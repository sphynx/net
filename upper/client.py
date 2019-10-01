from socket import *

HOST = 'localhost'
PORT = 12000

def main():
    client_socket = socket(AF_INET, SOCK_DGRAM)
    msg = input('Input lowercase sentence\n')
    client_socket.sendto(bytes(msg, "utf-8"), (HOST, PORT))
    received_msg, server_addr = client_socket.recvfrom(2048)
    print('Server answered: {}'.format(received_msg))
    client_socket.close()

if __name__ == '__main__':
    main()
