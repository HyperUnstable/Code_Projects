import socket
import time
import multiprocessing
host = "127.0.0.1"
port = 1223
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
cs, address = s.accept()
print("connected {0}".format(str(address)))
print("This is input server")

def snd():
    while True:
            datas = cs.send(input().encode("utf-8"))
        
snd()
