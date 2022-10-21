import socket
import sys


def Initial_Client():
    ip = socket.gethostname()
    port = 4508
    ADDRESS = (ip, port)
    # Second try-except block -- connect to given host/port
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(ADDRESS)
        Send_Passwrod_And_Username(client_socket)
    except socket.gaierror as e:
        print("Address-related error connecting to "
              "server: % s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)


def Send_Passwrod_And_Username(client_socket):
    while True:
        username = input('Enter Username :')
        if username.lower().strip() != 'e':
            password = input('Enter password :')
            connected = True
            while connected:
                try:
                    client_socket.send(username.encode())
                    client_socket.send(password.encode())
                    isValidUsername = client_socket.recv(1024).decode()
                    isValidPassword = client_socket.recv(1024).decode()
                    print(str(isValidUsername))
                    print("\n", str(isValidPassword))

                    username = input('Enter Username :')
                    password = input('Enter password :')
                except socket.error as e:
                    print("Error sending data: %s" % e)
                    sys.exit(1)

        else:
            client_socket.send(username.encode())
            data = client_socket.recv(1024).decode()
            print(str(data))
            break
        break
    client_socket.close()


Users = {}
if __name__ == '__main__':
    Initial_Client()
