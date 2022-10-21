import socket


def Initial_Server():
    iP = socket.gethostname()  # get the IP address
    port = 5058  # initiate port no above 1024
    ADDRESS = (iP, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDRESS)  # bind IP address and port together
    server_socket.listen(5)

    print("Server Waiting On port", port)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from client: ", conn.getpeername())
    responseRequests(conn)


def responseRequests(conn):
    while True:  # --- loop for receive
        request = conn.recv(1024).decode().lower()  # received data and decode it from bytes to string
        message = ''
        if request.lower().strip() != 'e':  # if data   received print it
            print("Client Send: ", str(request))
            if Users.keys().__contains__(request.split('|')[0]):
                message = 'account name : ' \
                          + request.split('|')[0] + '\t\t, Directory: ' + str(
                    Users[request.split('|')[0]]) + '\t\t,files count ' + str(
                    Directories[Users[request.split('|')[0]]].__len__())
                if request.split('|')[1] == 'g':  # if request to get files
                    for item in Directories[Users[request.split('|')[0]]]:
                        message = message + item + '\n'
                    if message == '':
                        message = 'no files'
                elif request.split('|')[1] == 's':  # if request to save new file
                    Directories[Users[request.split('|')[0]]].append(request.split('|')[2])
                    message = 'file saved : ' + request.split('|')[2]

                else:
                    message = 'unknown command'
            elif request.split('|')[1] == 'c':  # if request to create new account
                Users[request.split('|')[0]] = request.split('|')[2]
                Directories[request.split('|')[2]] = []
                message = 'account created :\n\t\t account name ' + \
                          request.split('|')[0] + '\n\t\t account directory ' + request.split('|')[2]
            else:
                message = 'f| account not found'
        else:
            message = "\n[server have been end the connection]..."
            conn.send(message.encode())
            break
        conn.send(message.encode())  # send data to the client, encoded from string to bytes
    conn.close()  # close the connection


Users = {}
Directories = {}
if __name__ == '__main__':
    Initial_Server()
