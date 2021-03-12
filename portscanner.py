import socket
from IPy import IP 

ip = input(" [+] Please insert your target ip to scan : ")
#port = int(input(" [+] Please insert your target port to scan :"))
port = 80 

try:
    sock =socket.socket()
    sock.connect(ip,port)
    print(" [+] Port 80 is open ")
except:
    print(" [-] port 80 is close ")

