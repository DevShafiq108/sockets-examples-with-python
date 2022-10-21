import socket
import re

# Make a regular expression
# for validating an Ip-address
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def Check_Port(port, conn):
    if 1024 < port <= 65535:
        return True
    else:
        return False


# Define a function for
# validate an Ip address
def check(conn, address):
    # pass the regular expression
    # and the string in search() method
    while True:  # --- loop for receive
        msg = conn.recv(1024).decode()
        message = list(msg.split(','))  # received data and decode it from bytes to string
        port = int(message[1])
        print(Check_Port(port, conn))
        if re.search(regex, message[0]) and Check_Port(port, conn):
            DecIpInfo[address[1]] = 1
            DecPortInfo[address[1]] = 1
            message = "\t\tValid Ip address And Port"
            conn.send(message.encode())

        else:
            if message == 'e' or DecIpInfo[address[1]] >= 3 or DecPortInfo[address[1]] >= 3:
                message = "\n[server have been end the connection]..."
                conn.send(message.encode())
                break
            else:
                if re.search(regex, message[0]) and not Check_Port(port, conn):
                    DecPortInfo[address[1]] += 1
                    message = "\t\tInvalid Port address"
                    conn.send(message.encode())
                elif not re.search(regex, message[0]) and Check_Port(port, conn):
                    DecIpInfo[address[1]] += 1
                    message = "\t\tInvalid Ip address"
                    conn.send(message.encode())
                else:
                    DecIpInfo[address[1]] += 1
                    DecPortInfo[address[1]] += 1
                    message = "\t\tInvalid Ip And Port address"
                    conn.send(message.encode())

    conn.close()  # close the connection


def Initial_Server():
    iP = ''  # get the IP address
    port = 8056  # initiate port no above 1024
    ADDRESS = (iP, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDRESS)  # bind IP address and port together
    server_socket.listen(5)

    print("Server Waiting On port", port)
    print(socket.getaddrinfo(iP, port))
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from client: ", conn.getpeername())
    if not DecIpInfo.keys().__contains__(address[1]) and not DecPortInfo.keys().__contains__(address[1]):
        DecIpInfo[address[1]] = 1
        DecPortInfo[address[1]] = 1
    check(conn, address)


DecIpInfo = {}
DecPortInfo = {}
if __name__ == '__main__':
    Initial_Server()
