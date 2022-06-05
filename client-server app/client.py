import socket
import uuid
import ipaddress
import sys


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

# send message to the server, check if the message sent
def send_to_server(channel, message):
    try:
        channel.sendall(str.encode(message))
    except socket.error:
        print("can't send on this channel")
        sys.exit(1)

# receive a message from the server, check if the message received
def receive_from_server(channel):
    try:
        return channel.recv(2048)
    except socket.error as e:
        print("can't receive on this channel")
        print(str(e))
        sys.exit(1)


def main():
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
        # TCP protocol by default
        client_control_socket = socket.socket()
        client_data_socket = socket.socket()
        client_control_socket.settimeout(30)
        client_data_socket.settimeout(30)
        client_control_socket.connect((host, port_control))
        client_data_socket.connect((host, port_data))
    except socket.error as e:
        print("Something want wrong with creating a socket, exiting...")
        print(str(e))
        sys.exit(1)

    # sending the unique MAC address
    # and receiving the unique server code on the control channel
    send_to_server(client_control_socket, identifier)
    code = receive_from_server(client_control_socket)
    # sending the message, MAC and the code from the server
    # and receiving a conformation (success or error) on the data channel
    send = message + ' ' + identifier + ' ' + code.decode()
    send_to_server(client_data_socket, send)
    answer = receive_from_server(client_data_socket)

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
