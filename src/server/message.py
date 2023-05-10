import datetime
import json

class Message:
    def __init__(self, sender: str, message: str):
        self.sender = sender
        self.message = message
        self.timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_json(self):
        return json.dumps(self.__dict__).encode('utf-8')

    @staticmethod
    def encode_message(message: str, sender: str):
        new_message = Message(sender, message)
        return json.dumps(new_message).encode('utf-8')

    @staticmethod
    def decode_message(data: bytes):
        return json.loads(data.decode('utf-8'))

    @staticmethod
    def server_message(message: str):
        message_to_send = Message(sender='server', message=message)
        return message_to_send.to_json()
