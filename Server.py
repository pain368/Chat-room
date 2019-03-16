import select
import socket
import threading


class MainServer:

    __ServerSetUp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __ip = ""
    __groupsocket = []
    __conn = ""
    __address: object = ""

    def __init__(self, ipaddress="0.0.0.0", port=5555):
        self.__ip = ipaddress
        self.port = port
        self.__ServerSetUp.bind((self.__ip, self.port))
        self.__ServerSetUp.setsockopt(socket.SO_REUSEADDR, socket.SOL_SOCKET, 1)

        print("[*][*]Waiting for a connection on: [{}:{}]".format(self.__ip, self.port))

    def runServer(self):

        self.__ServerSetUp.listen(5)


    def acceptConnection(self):


        conn, address = self.__ServerSetUp.accept()

        self.__conn = conn
        self.__address = address
        try:
            self.__groupsocket.append([self.__conn, self.__address])
            return self.__conn, self.__address
        except InterruptedError as err:
            print(err)

    @staticmethod
    def creatThread():
        pass

    def socketGroup(self):
        return self.socketGroup

    def sendData(self, send_data_on_client_socket, data_to_send):
        """That function send data on Client socket, 1st argument it's client socket from accept connection method,
        2nd argument is data for client """

        send_data_on_client_socket.send(data_to_send.encode('utf-8'))

        print("[*]Data sent successful[*]")

    def recvData(self, client_data):
        """"Function is responsibility for receiving data"""
        received_data = client_data.recv(2048)
        print("[*]Received data:[{}]".format(received_data))

        return received_data

    def showInfo(self, ip, port, socketList):
        """Method show general information about client address - IP, PORT NUMBER"""

        for i in self.socketList:
            line_separator = "------------------------------------------------------------------"
            print(i)
            print(line_separator)
            print("[*]Client socket: [{}:{}]".format(ip, port))
            print("[*]Client ip:")
            print("[*]Waiting for a connection")

    def closeConnection(self):
        self.__ServerSetUp.close()
