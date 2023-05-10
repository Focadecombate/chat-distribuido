import json
import socket


def encode_message(message):
    return json.dumps(message).encode("utf-8")


class SocketClient:
    def __init__(self, socket: socket.socket, buf_size=1024):
        self.socket = socket
        self.BufferSize = buf_size

    # solicita a lista de clients ao servidor
    def list_clients(self):
        self.socket.sendall(encode_message({"command": "listar_clients"}))

    # envia a mensagem para o client especificado
    def msg_client(self):
        nome_client = input("Digite o nome do client: ")

        mensagem = input("Digite a mensagem: ")

        self.socket.sendall(
            encode_message(
                {
                    "command": "msg_client",
                    "client_name": nome_client,
                    "message": mensagem,
                }
            )
        )

    # solicita a lista de grupos ao servidor
    def list_group(self):
        self.socket.sendall(encode_message({"command": "list_groups"}))

    # solicita a criação de um grupo ao servidor
    def create_group(self):
        nome_grupo = input("Digite o nome do grupo: ")

        self.socket.sendall(
            encode_message({"command": "create_group", "group_name": nome_grupo})
        )

    # solicita a entrada em um grupo ao servidor
    def join_group(self):
        nome_grupo = input("Digite o nome do grupo: ")

        self.socket.sendall(
            encode_message({"command": "join_group", "group_name": nome_grupo})
        )

    # envia a mensagem para o grupo especificado
    def msg_group(self):
        nome_grupo = input("Digite o nome do grupo: ")
        mensagem = input("Digite a mensagem: ")

        self.socket.sendall(
            encode_message(
                {"command": "msg_group", "group_name": nome_grupo, "message": mensagem}
            )
        )

    # solicita a saída de um grupo ao servidor
    def leave_group(self):
        nome_grupo = input("Digite o nome do grupo: ")

        self.socket.sendall(
            encode_message({"command": "leave_group", "group_name": nome_grupo})
        )

    # solicita a exclusão de um grupo ao servidor
    def delete_group(self):
        nome_grupo = input("Digite o nome do grupo: ")

        self.socket.sendall(
            encode_message({"command": "delete_group", "group_name": nome_grupo})
        )

    def leave_server(self):
        self.socket.sendall(encode_message({"command": "leave_server"}))
