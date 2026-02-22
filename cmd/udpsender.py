import signal
import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('127.0.0.1', 42069)

def sigint_handler(signal, frame):
    print("Bye, bye!")
    client_sock.close()
    exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def sendChannel():
    while True:
        bstr = input("> ").encode('utf-8')
        if not bstr:
            continue
        client_sock.sendto(bstr, addr)


def main():
    sendChannel()


if __name__ == "__main__":
    main()
