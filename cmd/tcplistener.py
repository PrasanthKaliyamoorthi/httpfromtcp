import signal
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('127.0.0.1', 42069))
server_sock.listen(10)
c_conn, c_addr = server_sock.accept()

def sigint_handler(signal, frame):
    print("Bye, bye!")
    server_sock.close()
    exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def listenChannel():
    line = ""
    while True:
        bstr = c_conn.recv(8).decode('utf-8')
        if not bstr:
            break
        if not '\n' in bstr:
            line += bstr
            continue
        parts = bstr.split('\n')
        line += parts[0]

        tmp = line
        line = parts[1]
        yield tmp

def main():

    for line in listenChannel():
        print(f"Read : {line}")


if __name__ == "__main__":
    main()
