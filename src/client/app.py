from src.common import Config
from socket_client import SocketClient
from print_commands import print_commands

import socket


class App:
    def __init__(self, config: Config, client_socket: socket.socket) -> None:
        self.config = config
        self.open_client_socket = client_socket
        self.socket_client = SocketClient(self.open_client_socket, config.BUFFER_SIZE)

    def start_client(self):
        response = self.open_client_socket.recv(self.config.BUFFER_SIZE).decode("utf-8")

        nome = input(response)

        self.open_client_socket.sendall(str.encode(nome))

        print(self.open_client_socket.recv(self.config.BUFFER_SIZE).decode("utf-8"))

    def prompt(self):
        while True:
            command = input("Digite o comando: ")

            if command == "1":
                self.socket_client.list_clients()

            elif command == "2":
                self.socket_client.msg_client()

            elif command == "3":
                self.socket_client.list_group()

            elif command == "4":
                self.socket_client.create_group()

            elif command == "5":
                self.socket_client.join_group()

            elif command == "6":
                self.socket_client.msg_group()

            elif command == "7":
                self.socket_client.leave_group()

            elif command == "8":
                self.socket_client.delete_group()

            elif command == "quit":
                self.socket_client.leave_server()
                self.open_client_socket.close()
                break

            elif command == "help":
                print_commands()

            else:
                print("Comando inválido.")
