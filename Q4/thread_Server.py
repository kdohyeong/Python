import socket
import argparse
import os
import threading

def run_server(port=4000):
    host = ''
    while True:
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
            s.bind((host,port))
            s.listen(5)

            conn, addr = s.accept()
            print("Connected to : ", addr[0], addr[1])
            

            t = threading.Thread(target = R_Send ,args = (conn, addr))
            t.deamon = True
            t.start()
            
def R_Send(conn, addr):
    msg = conn.recv(1024)
    Text = msg.decode()
    print("Receive From Client : ", Text)
    Reverse_Text = Text[::-1]

    conn.sendall(str(Reverse_Text).encode())
    print("Send to Reverse_Text : ", Reverse_Text)
    conn.close()
    print(addr[0], addr[1], " : Connect Closed")
        
if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument('-p', help="port_number", required=True)
    


    args = parser.parse_args()

    run_server(int(args.p))

    