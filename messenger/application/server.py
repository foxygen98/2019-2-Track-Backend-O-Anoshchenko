#! /usr/bin/python3

import socket

def main():
    socket_server = socket.socket(sock.AF_INET, sock.SOCK_STREAM)
    socket_server.bind(('', 8090))
    socket_server.listen(5)
    while True:
        client_socket, addr = socket_server.accept()
        data = b''
        tmp = client_socket.recv(1024)
        while tmp:
            data += tmp
            tmp = client_socket.recv(1024)
        print(data.upper().decode('utf8'))
        socket_server.close()

if __name__ == "__main__":
    main()