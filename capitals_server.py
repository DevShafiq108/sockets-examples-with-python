import socket


def Initial_Server():
    try:
        iP = socket.gethostname()  # get the IP address
        port = 5502  # initiate port no above 1024
        ADDRESS = (iP, port)

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(ADDRESS)  # bind IP address and port together
        server_socket.listen(5)

        print("Server Waiting On port", port)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from client by Conn: ", conn.getpeername())
        Get_Capital_Of_Country(conn)
    except socket.error as e:
        print(e)


def Get_Capital_Of_Country(conn):
    while True:  # --- loop for receive
        message = conn.recv(1024).decode()  # received data and decode it from bytes to string
        if message.lower().strip() != 'e':  # if data   received print it
            print("Client Send: ", str(message))
        else:
            message = "\n[server have been end the connection]..."
            conn.send(message.encode())
            break
        message = f"\t\tCapital of {message} Is: {Capitals.get(message.lower())}"
        conn.send(message.encode())  # send data to the client, encoded from string to bytes
    conn.close()  # close the connection


Capitals = {
    'jordan': 'Amman',
    'libya': 'Tripoli',
    'kuwait': 'Kuwait City',
    'egypt': 'Cairo',
    'morocco': 'Rabat',
    'qatar': 'Doha',
    'yemen': 'Sana’a',
    'uae': 'Abu Dhabi',
    'bahrain': 'Manama',
    'tunisia': 'Tunis',
    'sudan': 'Khartoum',
    'oman': 'Muscat',
    'syria': 'Damascus',
    'algeria': 'Algiers',
    'saudi Arabia': 'Riyadh',
    'iraq': 'Baghdad',
    'djibouti': 'Djibouti',
    'mauritania': 'Nouakchott',
    'somalia': 'Mogadishu',
    'palestine': 'Ramallah/ Jerusalem',
    'lebanon': 'Beirut'
}
if __name__ == '__main__':
    Initial_Server()
