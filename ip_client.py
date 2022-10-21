import socket


def Initial_Client():
    iP = socket.gethostname()  # as both code is running on same pc
    port = 8056  # socket server port number
    ADDRESS = (iP, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDRESS)  # connect to the server

    Ip_Validit(client_socket)


def Ip_Validit(client_socket):
    while True:
        message = input("Enter Your Ip Address And Port Number separated by Comma Or enter E To End Program -> ")  # take input
        while True:
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(str(data))
            message = input("Enter Your Ip Address Or enter E To End Program -> ")  # again take input
            if message == "e":
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print(str(data))
                break
        break
    client_socket.close()  # close the connection


if __name__ == '__main__':
    Initial_Client()
