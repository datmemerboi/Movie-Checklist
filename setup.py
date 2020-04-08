'''
This is the file to setup your system for Movie Checklist on Debian-based system.
Avoid it if you have the softwares pre-installed.

Softwares Required: Python3 software, PyQt5, MongoDB, PyMongo & Firebase modules
'''

# Installing PyQt5
import os
print("Installing PyQt5..")
os.system("pip3 install --user pyqt5")
os.system("sudo apt-get install python3-pyqt5")

# Installing requirements.txt
print("Installing necessary modules..")
os.system("sudo apt-get install python3-pip")
os.system("python3 -m pip3 install -r requirements.txt")