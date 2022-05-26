import socket
import uuid
import ipaddress


# check if an IP address is valid (IPv4 or IPv6)
def validate_ip_address(address):
    if address == 'localhost':
        return True
    try:
        ip = ipaddress.ip_address(address)
        return True
    except ValueError:
        print(f'{address} is an invalid IP address')
        return False


def main():
    # TCP protocol by default
    ClientControlSocket = socket.socket()
    ClientDataSocket = socket.socket()
    ClientControlSocket.settimeout(30)
    ClientDataSocket.settimeout(30)
    portControl = 8000
    portData = 8001
    # a unique MAC address for every computer
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
        ClientControlSocket.connect((host, portControl))
        ClientDataSocket.connect((host, portData))
    except socket.error as e:
        print(str(e))
        # error - exit the main
        return
    # sending the unique MAC address
    # and receiving the unique server code on the control channel
    try:
        ClientControlSocket.sendall(str.encode(identifier))
        code = ClientControlSocket.recv(2048)
    except socket.error as e:
        print(str(e))
        # error - exit the main
        return

    # sending the message, MAC and the code from the server
    # and receiving a conformation (success or error) on the data channel
    send = message + ' ' + identifier + ' ' + code.decode()
    ClientDataSocket.sendall(str.encode(send))
    answer = ClientDataSocket.recv(2048)

    # returning an answer to the client
    if answer == b'error':
        print('The message was not delivered to the server')
    else:
        print('The message was delivered successfully')

    # close all resources
    ClientControlSocket.close()
    ClientDataSocket.close()


if __name__ == '__main__':
    main()
