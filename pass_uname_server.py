import socket
import sys


def Initial_Server():
    ip = socket.gethostname()
    port = 4508
    ADDRESS = (ip, port)
    # First try-except block -- create socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(ADDRESS)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    print(f'[SERVER IS STARTING]...')
    server_socket.listen(5)
    print(f'[SERVER IS STARTING IN PORT ({port})]')

    client, address = server_socket.accept()
    Check_Validity_Of_Passwrod_And_Username(client)


def Check_Validity_Of_Passwrod_And_Username(server_socket):
    while True:
        username = server_socket.recv(1024).decode()
        user = username.lower().strip()
        flag = False
        if username != 'e':
            password = server_socket.recv(1024).decode()
            if USERS.keys().__contains__(username.lower().strip()):
                username = "User Name Is Valid"
                flag = True
            else:
                username = "User Name Is Invalid"
                # server_socket.send(username.encode())

            if flag and USERS[user].__eq__(password):
                password = "password Is Valid"
            else:
                password = "password Is Invalid"

        # server_socket.send(password.encode())

        else:
            username = "\n[server have been end the connection]..."
            server_socket.send(username.encode())
            break
        server_socket.send(username.encode())
        server_socket.send(password.encode())
    server_socket.close()


USERS = {
    'shafiq': '12345',
    'ali': '3355',
    'faisal': '00000',
    'akram': '33001',
    'naser': '54321'
}
if __name__ == '__main__':
    Initial_Server()
