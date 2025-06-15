import socket
import time
import sys
from commands import LaCrocCommands


def client_program(host, port=33333):
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    for i in range(10):
        time.sleep(2)
        client_socket.send(LaCrocCommands.talk.value.encode())  # send message

    client_socket.close()  # close the connection

from commands import LaCrocCommands
import socket
import os
import re

def find_command(inp: str) -> LaCrocCommands:
    for command in LaCrocCommands:
        search = re.findall(command.value, inp)
        if any(search):
            return command
    return None

def comm(host=None, port=33333):
    if host is None:
        host = os.environ["LECROC_SERVER"]
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print(f"Connected! Host: {host} Port: {port}")
    def send_command(message: str):
        client_socket.send(message.encode())  # send message
    return send_command


if __name__ == '__main__':
    client_program(sys.argv[1])