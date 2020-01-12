import socket
import argparse
import os


def run_server(port=4000):
    host = ''

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen(1)

        conn, addr = s.accept()
        msg = conn.recv(1024)
        
        line = args.d +'/'+ msg.decode()

        if ".txt" in line :
            GetFile = open("C:/Users/KDHyeong/Desktop/Python/Python/" + line , 'rt')
            FileData = GetFile.read()
            GetFile.close()
            conn.sendall(FileData.encode())
            
        else :
            GetFile = open("C:/Users/KDHyeong/Desktop/Python/Python/" + line , 'rb')
            FileData = GetFile.read()
            GetFile.close()
            conn.sendall(FileData)

        print("Send to Client : " + msg.decode())
        conn.close()
        
if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-d', help="file directory", required=True)


    args = parser.parse_args()
    run_server(port=int(args.p))
    
    