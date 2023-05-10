from termcolor import colored

import json
import socket


def receive_messages(client_socket: socket.socket, BUFFER_SIZE=1024):
    while True:
        message = ""
        try:
            message = client_socket.recv(BUFFER_SIZE).decode()

            if not message:
                print("close")
                break

            message_obj = json.loads(message)
            if message_obj["sender"] == "server":
                server_message = f"\n  {message_obj['message']}"
                print(colored(server_message, "blue"))
                continue

            user_message = f"\n  Nova mensagem de {message_obj['sender']}:\n  {message_obj['message']}\n  data: {message_obj['timestamp']} \n"

            print(colored(user_message, "green"))

        except Exception as error:
            print("Erro ao receber mensagem", error, message)
