import socket


def Initial_Client():
    iP = socket.gethostname()  # as both code is running on same pc
    port = 5058  # socket server port number
    ADDRESS = (iP, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDRESS)  # connect to the server

    requestAccount(client_socket)


def requestAccount(client_socket):
    lastAccName = input(
        "Enter Account Name -> ")
    connected = True
    while connected:
        opNum = input(
            "Enter Operation num:\n 1- create account\n 2- request files\n 3- upload new files\n  Or enter E To End Program -> ")  # take input
        message = lastAccName
        if opNum.lower().strip() != 'e':
            # take input
            if opNum == '1':
                lastAccName = input("Enter Account Name -> ")
                dirName = input("Enter Directory Name -> ")  # take input
                message = lastAccName + '|c|' + dirName
            elif opNum == '2':
                message = lastAccName + '|g'
            elif opNum == '3':
                fileName = input(
                    "Enter New File Name -> ")  # take input
                message = lastAccName + '|s|' + fileName
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print("Server Send: ", str(data).upper())
        else:

            client_socket.send(opNum.encode())
            data = client_socket.recv(1024).decode()
            print(str(data))
            break
    client_socket.close()  # close the connection


if __name__ == '__main__':
    Initial_Client()
