import socket
from _thread import *
import threading
import hashlib


def main():
    # TCP protocol by default
    ServerControlSocket = socket.socket()
    ServerDataSocket = socket.socket()
    # the server will start working at the computer that it is running on
    host = 'localhost'
    portControl = 8000
    portData = 8001
    clientCount = 0

    # connect the host and ports to the socket server
    # for both control and data channels
    try:
        ServerControlSocket.bind((host, portControl))
        ServerDataSocket.bind((host, portData))
    except socket.error as e:
        print(str(e))
        return

    # The server is listening on the ports for clients
    ServerControlSocket.listen()
    ServerDataSocket.listen()
    print('Server is listening..')

    # The server is always working, need to stop it manually
    while True:
        # get the client sockets
        clientControl, addressC = ServerControlSocket.accept()
        clientData, addressD = ServerDataSocket.accept()
        print('Control channel connected to: ' + addressC[0] + ':' + str(addressC[1]))
        print('Data channel connected to: ' + addressD[0] + ':' + str(addressD[1]))
        # start the treads, for multiple clients
        start_new_thread(control_channel, (clientControl,))
        start_new_thread(data_channel, (clientData,))
        clientCount += 1
        print('Client number: ' + str(clientCount))


# save all the clients MACs and codes in tuples
# clients is a set of tuples so if a client is already in the set, he will not be added again
# for clients that wants to connect to the server several times - the MAC and code will be the same
# I used a set to save space and time - just adding no need to remove or to check if the client is already in the set
clients = set()
# a lock for mutual exclusion between threads
lock = threading.Lock()


# write the message to the log file
def write_to_log(message):
    with open('logfile.txt', 'a') as logFile:
        logFile.write(message + '\n')


# handler for control channel port 8000
def control_channel(connection):
    unique = connection.recv(2048)
    # use the sha-1 hash function to generate a unique code, a better hash function than the default one (hash())
    code = str(hashlib.sha1(unique).hexdigest())
    # send the code to the client
    connection.sendall(str.encode(code))
    # encode the code to bytes to match the code received from the data channel
    code = code.encode()
    # protect mutual resource
    lock.acquire()
    clients.add((unique, code))
    lock.release()
    connection.close()


# handler for data channel port 8001
def data_channel(connection):
    # this flag indicates if the message was written to the log file
    flag = False
    message = connection.recv(2048)
    message = message.split()
    # message = message + ' ' + identifier + ' ' + str(code)
    # message[0] = message
    # message[1] = identifier
    # message[2] = code

    # protect critical code
    lock.acquire()
    for unique, code in clients:
        if unique == message[1] and code == message[2]:
            flag = True
            # write a string to the file, not bytes
            mess = message[0].decode()
            write_to_log(mess)
            break
    lock.release()
    if not flag:
        connection.sendall(str.encode('error'))
    else:
        connection.sendall(str.encode('success'))
        connection.close()


if __name__ == '__main__':
    main()
