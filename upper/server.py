from socket import *

PORT = 12000


def main():
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', PORT))
    print('server is ready to receive')

    while True:
        msg, client_addr = server_socket.recvfrom(2048)
        host, port = client_addr
        print('client connected: {} {}'.format(host, port))
        modified_msg = msg.upper()
        server_socket.sendto(modified_msg, client_addr)


if __name__ == '__main__':
    main()
