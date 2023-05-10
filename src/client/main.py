import socket
import threading
from app import App
from receive_messages import receive_messages
from print_commands import print_commands
from Config import Config


if __name__ == "__main__":
    config = Config()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((config.HOST, config.PORT))

    app = App(config, client_socket)
    app.start_client()
    receive_thread = threading.Thread(
        target=receive_messages, args=(client_socket, config.BUFFER_SIZE)
    )
    receive_thread.start()
    print_commands()
    app.prompt()
