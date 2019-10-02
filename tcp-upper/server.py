from socket import *

PORT = 12002


def serve():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', PORT))
    sock.listen(5)

    while True:
        client, addr = sock.accept()
        print('client connected:', addr)

        while True:
            msg = client.recv(4096)
            if msg:
                print('got:', msg)
                client.send(msg.upper())
            else:
                client.close()
                break

if __name__ == '__main__':
    serve()
