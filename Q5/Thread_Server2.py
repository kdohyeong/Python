import socket
import argparse
import os
import threading
import time

def run_server(port=4000):
    host = ''
    while True:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
            s.bind((host,port))
            s.listen(1)

            conn, addr = s.accept()
            print("Connected to : ", addr[0], addr[1])
            
            t1 = threading.Thread(target = Send ,args = (conn, addr))
            t2 = threading.Thread(target = Receive , args = (conn , addr))
            t1.deamon = True
            t2.deamon = True
            t1.start()
            t2.start()


def Receive(conn, addr):
    while True:
        msg = conn.recv(1024)
        Text1 = msg.decode()
        print("\nMassage From Client ", addr[0] , addr[1] ,">>>>",Text1)
        print("\nInput Massage : ")
        time.sleep(1)

def Send(conn, addr):
    while True:
        Text2 = input("\nInput Massage : \n")
        conn.sendall(Text2.encode())
        
        
if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument('-p', help="port_number", required=True)
    


    args = parser.parse_args()

    run_server(int(args.p))

    