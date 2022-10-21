import socket


def Initial_Client():
    iP = socket.gethostname()  # as both code is running on same pc
    port = 5057  # socket server port number
    ADDRESS = (iP, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDRESS)  # connect to the server

    Send_Message_In_lowerCase(client_socket)


def Send_Message_In_lowerCase(client_socket):
    while True:
        message = input("Enter Your Word Or enter E To End Program -> ")  # take input
        while True:
            if message.lower().strip() != 'e':
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print("Server Send: ", str(data))
                message = input("Enter Your Word Or enter E To End Program -> ")  # again take input
            else:
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                print(str(data))
                break
        break
    client_socket.close()  # close the connection


if __name__ == '__main__':
    Initial_Client()
