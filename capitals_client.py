import socket


def Initial_Client():
    iP = socket.gethostname()  # as both code is running on same pc
    port = 5502  # socket server port number
    ADDRESS = (iP, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDRESS)  # connect to the server

    Send_Country_Name(client_socket)


def Send_Country_Name(client_socket):
    while True:
        message = input("Enter Country You Want to get her Capital Or enter E To End Program -> ")  # take input
        connected = True
        while connected:
            if message.lower().strip() != 'e':
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print(str(data))
                message = input("Enter Country You Want to get her Capital Or enter E To End Program -> ")  # take input
            else:
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print(str(data))
                break
        break
    client_socket.close()  # close the connection


if __name__ == '__main__':
    Initial_Client()
