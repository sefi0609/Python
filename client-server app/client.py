import socket
import uuid
import ipaddress


# check if an IP address is valid (IPv4 or IPv6)
def validate_ip_address(address):
    if address == 'localhost':
        return True
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        print(f'{address} is an invalid IP address')
        return False


def main():
    # TCP protocol by default
    client_control_socket = socket.socket()
    client_data_socket = socket.socket()
    client_control_socket.settimeout(30)
    client_data_socket.settimeout(30)
    port_control = 8000
    port_data = 8001
    identifier = hex(uuid.getnode())

    # for localhost enter 127.0.0.1 or 'localhost', if the server and the client are on the same computer
    while True:
        host = input('Please enter the host IP or localhost: ')
        if validate_ip_address(host):
            break
        else:
            pass
    message = input('Please enter a massage for the server: ')

    # connecting to control and data channels
    print('Waiting for connection response')
    try:
        client_control_socket.connect((host, port_control))
        client_data_socket.connect((host, port_data))
    except socket.error as e:
        print(str(e))
        # error - exit the main
        return
    # sending the unique MAC address
    # and receiving the unique server code on the control channel
    try:
        client_control_socket.sendall(str.encode(identifier))
        code = client_control_socket.recv(2048)
    except socket.error as e:
        print(str(e))
        # error - exit the main
        return

    # sending the message, MAC and the code from the server
    # and receiving a conformation (success or error) on the data channel
    send = message + ' ' + identifier + ' ' + code.decode()
    client_data_socket.sendall(str.encode(send))
    answer = client_data_socket.recv(2048)

    # returning an answer to the client
    if answer == b'error':
        print('The message was not delivered to the server')
    else:
        print('The message was delivered successfully')

    # close all resources
    client_control_socket.close()
    client_data_socket.close()


if __name__ == '__main__':
    main()
