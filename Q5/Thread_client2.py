import socket
import argparse
import threading
import time


def run(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print ("Connected Success")
        
        t = threading.Thread(target = Receive , args = (s, ))
        t.daemon = True
        t.start()

        while True :
           
            line = input("\nInput Massage : \n")
            s.send(line.encode())
            
        
        


def Receive(s):
    while True:
          
        resp = s.recv(1024)
        print("\nMassage From Server >>>> " ,resp.decode())
        print("\nInput Massage : ")
        time.sleep(1)  


if __name__ == '__main__' :

    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)
    
    args = parser.parse_args()
    run(host=args.i, port=int(args.p))