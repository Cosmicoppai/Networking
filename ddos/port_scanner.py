# it'll search an open port in network. It's Illegal

import socket, threading
from queue import Queue

target = "172.67.196.53"
queue = Queue()
open_ports = []


def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET tells that the socket is an internet socket & SOCK_STREAM tells that it's an UDP connection
        sock.connect((target, port))
        return True

    except:
        return False


for i in range(800, 65000, 10):
    queue.put(i)


def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            open_ports.append(port)


thread_list = []

for t in range(5000):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports:- ", open_ports)