from models import Client, Group
from message import Message


class GroupService:
    def __init__(self, groups: dict[str, Group]):
        self.groups = groups

    def list_group(self):
        return "Grupos disponíveis: " + ", ".join(self.groups.keys())

    def find_group(self, group_name: str):
        return self.groups.get(group_name, None)

    def is_client_in_group(self, search_client: Client, group: Group):
        return next(
            (client for client in group.clients if client.name == search_client.name),
            None,
        )

    def group_not_found(self, client: Client, group_name: str):
        client.conn.sendall(
            Message.server_message(f"Grupo {group_name} não encontrado")
        )

    def not_in_group(self, client: Client, group_name: str):
        client.conn.sendall(
            Message.server_message(f"Você não está no grupo {group_name}")
        )

    def send_message_to_group(self, sender: Client, group_name: str, message: str):
        group = self.find_group(group_name)

        if group == None:
            self.group_not_found(sender, group_name)
            return

        sender_in_group = next(
            (client for client in group.clients if client.name == sender.name), None
        )

        if sender_in_group == None:
            sender.conn.sendall(
                Message.server_message(f"Você não está no grupo {group_name}")
            )
            return

        print("Enviando mensagem para o grupo", group.name, message)

        new_message = Message(sender=sender.name, message=message)

        for member in group.clients:
            if member.name == sender.name:
                continue
            print("Membro: ", member.name)
            member.conn.sendall(new_message.to_json())

        sender.conn.sendall(Message.server_message("Mensagem enviada ao grupo"))

    def server_send_message_to_group(self, group_name: str, message: str):
        group = self.find_group(group_name)

        if group == None:
            return

        print("Enviando mensagem para o grupo", group.name, message)

        new_message = Message(sender="server", message=message)

        for member in group.clients:
            print("Membro: ", member.name)
            member.conn.sendall(new_message.to_json())

    def create_group(self, client: Client, group_name: str):
        found_group = self.find_group(group_name)

        if found_group != None:
            self.group_not_found(client, group_name)
            return

        new_group = Group(group_name)
        new_group.clients.append(client)
        self.groups[group_name] = new_group

        client.groups.append(new_group)
        client.conn.sendall(Message.server_message("Você criou o grupo"))

    def join_group(self, client: Client, group_name: str):
        found_group = self.find_group(group_name)

        if found_group == None:
            self.group_not_found(client, group_name)
            return

        client_in_group_already = self.is_client_in_group(client, found_group)

        if client_in_group_already != None:
            client.conn.sendall(
                Message.server_message(f"Você já está no grupo {group_name}")
            )
            return


        found_group.clients.append(client)
        client.groups.append(found_group)
        message = f"{client.name} juntou-se ao grupo {group_name}"

        self.server_send_message_to_group(group_name=group_name, message=message)

    def leave_group(self, client: Client, group_name: str):
        found_group = self.find_group(group_name)

        if found_group == None:
            self.group_not_found(client, group_name)
            return

        client_in_group_already = self.is_client_in_group(client, found_group)

        if client_in_group_already == None:
            self.not_in_group(client, group_name)
            return

        message = f"{client.name} saiu do grupo {group_name}"

        self.server_send_message_to_group(group_name=group_name, message=message)

        found_group.clients.remove(client)
        client.groups.remove(found_group)

        client.conn.sendall(Message.server_message("Você saiu do grupo"))

    def delete_group(self, client: Client, group_name: str):
        found_group = self.find_group(group_name)

        if found_group == None:
            self.group_not_found(client, group_name)
            return

        client_in_group_already = self.is_client_in_group(client, found_group)

        if client_in_group_already == None:
            self.not_in_group(client, group_name)
            return

        message = f"{client.name} deletou o grupo {group_name}"

        self.server_send_message_to_group(group_name=group_name, message=message)

        for member in found_group.clients:
            member.groups.remove(found_group)

        del self.groups[group_name]

        client.conn.sendall(Message.server_message("Você deletou o grupo"))
