from models import Client
from message import Message


class ClientService:
    def __init__(self, clients: list[Client]):
        self.clients = clients

    def list_clients(self):
        return "Clientes conectados: " + ", ".join(
            map(lambda client: client.name, self.clients)
        )

    def find_client(self, client_name: str):
        client = next(
            (client for client in self.clients if client.name == client_name), None
        )
        return client

    def send_message_to_client(self, sender: Client, client_name: str, message: str):
        found_client = self.find_client(client_name)

        if found_client == None:
            sender.conn.sendall(Message.server_message("Cliente não encontrado"))
            return

        print("Enviando mensagem para o cliente", found_client.name, message)

        new_message = Message(sender.name, message)

        found_client.conn.sendall(new_message.to_json())

        sender.conn.sendall(Message.server_message("Mensagem enviada ao cliente"))
