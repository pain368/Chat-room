import threading
import Server
import clientLoop
from Server import MainServer

if __name__ == "__main__":

    server = MainServer()

    threads = []

    try:
        while True:
            server.runServer()
            client_socket, client_address = server.acceptConnection()

    except KeyboardInterrupt:

        server.closeConnection()

