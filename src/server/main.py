import socket
import threading

from Config import Config

from models import Group, Client
from client_service import ClientService
from group_service import GroupService
from message import Message

config = Config()
clients: list[Client] = []
groups: dict[str, Group] = {}
group_service = GroupService(groups)
clients_service = ClientService(clients)


def handle_client(conn: socket.socket, addr):
    conn.send(b"Qual o seu nome? ")

    name = conn.recv(config.BUFFER_SIZE).decode("utf-8")

    client = Client(conn=conn, addr=addr, name=name)
    clients.append(client)

    conn.send(b"Seja bem-vindo, " + name.encode("utf-8"))

    print("Conexão estabelecida por ", addr)
    print("Clients conectados: ", clients)

    while True:
        data = conn.recv(config.BUFFER_SIZE)

        if not data:
            print("Empty message received. Closing connection.", client.name)
            break

        message = Message.decode_message(data)

        if message == None or "command" not in message:
            conn.sendall(Message.server_message("Comando inválido").encode())
            continue

        command: str = message["command"]

        if command == "listar_clients":
            clients_to_send = clients_service.list_clients()

            message = Message.server_message(clients_to_send)
            conn.sendall(message)
            continue

        elif command == "msg_client":
            clients_service.send_message_to_client(
                sender=client,
                client_name=message["client_name"],
                message=message["message"],
            )

        elif command == "list_groups":
            conn.sendall(Message.server_message(group_service.list_group()))

        elif command == "msg_group":
            group_service.send_message_to_group(
                sender=client,
                group_name=message["group_name"],
                message=message["message"],
            )

        elif command == "join_group":
            group_service.join_group(
                client=client,
                group_name=message["group_name"],
            )

        elif command == "create_group":
            group_service.create_group(
                client=client,
                group_name=message["group_name"],
            )

        elif command == "leave_group":
            group_service.leave_group(
                client=client,
                group_name=message["group_name"],
            )

        elif command == "delete_group":
            group_service.delete_group(
                client=client,
                group_name=message["group_name"],
            )

    conn.close()
    print("Conexão encerrada por", addr)
    for group in groups.values():
        if client in group.clients:
            group.clients.remove(client)
    clients.remove(client)
    print("Clientes Conectados: ", clients)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((config.HOST, config.PORT))
        s.listen(1000)

        print("Servidor escutando em", (config.HOST, config.PORT))

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            print(f"threads: {threading.active_count()+1}")
            thread.start()


if __name__ == "__main__":
    start_server()
