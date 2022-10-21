import socket


def Initial_Server():
    iP = socket.gethostname()  # get the IP address
    port = 5057  # initiate port no above 1024
    ADDRESS = (iP, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDRESS)  # bind IP address and port together
    server_socket.listen(5)

    print("Server Waiting On port", port)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from client: ", conn.getpeername())
    Convert_Lower_To_Upper(conn)



def Convert_Lower_To_Upper(conn):
    while True:  # --- loop for receive
        message = conn.recv(1024).decode()  # received data and decode it from bytes to string
        if message.lower().strip() != 'e':  # if data   received print it
            print("Client Send: ", str(message))
        else:
            message = "\n[server have been end the connection]..."
            conn.send(message.encode())
            break
        conn.send(message.encode().upper())  # send data to the client, encoded from string to bytes
    conn.close()  # close the connection


if __name__ == '__main__':
    Initial_Server()


