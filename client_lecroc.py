import socket
import time
import sys
from commands import LaCrocCommands


def client_program(host, port=33333):
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    for i in range(10):
        time.sleep(2)
        client_socket.send(LaCrocCommands.talk.encode())  # send message

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program(sys.argv[1])