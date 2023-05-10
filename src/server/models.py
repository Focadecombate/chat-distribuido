import socket


class Client:
    def __init__(self, conn: socket.socket, addr, name: str):
        self.conn = conn
        self.addr = addr
        self.name = name
        self.groups: list[Group] = []


class Group:
    def __init__(self, name: str):
        self.name = name
        self.clients: list[Client] = []