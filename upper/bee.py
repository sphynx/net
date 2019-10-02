from socket import *
from threading import Thread
import random
import string
import sys
import time

HOST = 'localhost'
PORT = 12000


reqs = 0
def monitor():
    '''Monitor performance, David Beazley's style :)'''

    global reqs
    while True:
        time.sleep(1)
        if reqs:
            print(reqs, 'reqs/sec')
            reqs = 0
        else:
            break


def sting(requests, delay=0):
    '''Sends many requests to the server, possibly with delay
    between them'''

    global reqs

    sock = socket(AF_INET, SOCK_DGRAM)

    letters = bytes(string.ascii_lowercase, 'ascii')

    start = time.perf_counter()

    for i in range(1, requests + 1):
        str_len = random.randint(1, 10)
        random_str = bytes(random.choices(letters, k=str_len))
        # print(f'sting #{i}: {random_str}')
        sock.sendto(random_str, (HOST,PORT))

        time.sleep(delay)
        reqs += 1

    end = time.perf_counter()

    print("total time taken: {:.2f}s".format(end - start))


def main():
    Thread(target=monitor, daemon=True).start()

    if len(sys.argv) < 2:
        sting(10)
    elif len(sys.argv) == 2:
        reqs = int(sys.argv[1])
        sting(reqs)
    else:
        reqs = int(sys.argv[1])
        delay = int(sys.argv[2])
        sting(reqs, delay)


if __name__ == '__main__':
    main()


