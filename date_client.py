import socket


def Initial_Client():
    iP = socket.gethostname()  # as both code is running on same pc
    port = 5055  # socket server port number
    ADDRESS = (iP, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDRESS)  # connect to the server

    Get_Date_And_Time(client_socket)


def Get_Date_And_Time(client_socket):
    while True:
        message = input("Are You Want To Get The Current Date And Time ?"
                        "Enter [Yes/Y] If Ok OR enter E To End Program -> ")  # take input
        connected = True
        while connected:
            if message.lower().strip() != 'e' and message.lower().strip() == 'y' \
                    or message.lower().strip() == 'yes':
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print('The Current Date And Time:', str(data))
                message = input("Are You Want To Get The Current Date And Time ?"
                                "Enter [Yes/Y] If Ok OR enter E To End Program -> ")  # take input
            else:
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print(str(data))
                break
        break
    client_socket.close()  # close the connection


if __name__ == '__main__':
    Initial_Client()
