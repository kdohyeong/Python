import socket
import argparse
import os

def run(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        line = args.f
        print("File name : ", line)
        s.sendall(line.encode())
        resp = s.recv(1024)
        
        GetFile = open("C:/Users/KDHyeong/Desktop/Python/Python/Q3/" + line , 'w')
        GetFile.write(resp.decode())
        GetFile.close()

        print("File Reception Success : " + line)
        size = os.path.getsize("C:/Users/KDHyeong/Desktop/Python/Python/Q3/" + line)
        print("File Size : ", size)
       

if __name__ == '__main__' :

    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)
    parser.add_argument('-f', help="file_name", required=True)
    
    args = parser.parse_args()
    run(host=args.i, port=int(args.p))