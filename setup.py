"""
This is the file to setup your system for Movie Checklist.
Avoid it if you have the softwares pre-installed.

Softwares Required: Python3, PyQt5, MongoDB, PyMongo
"""

# Installing PyQt5
import os
os.system("pip3 install --user pyqt5")
os.system("sudo apt-get install python3-pyqt5")
os.system("qtchooser -run-tool=designer -qt=5")

# Installing PyMongo
os.system("python3 -m pip install pymongo")