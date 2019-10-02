from socket import *

HOST = 'localhost'
PORT = 12000


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))
    print('connected ok')
    sock.send(b'hello')
    msg = sock.recv(4096)
    print('got from server:', msg)
    sock.close()

if __name__ == '__main__':
    main()
