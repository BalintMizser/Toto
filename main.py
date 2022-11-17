from funcions import menu, readFromFile, kiir, beker
from data import kerdesek, eredmenyek

import time
choice= ''
while choice != '0':
    choice = menu()
    if choice == '1':
        readFromFile()
        #kiir()
        beker()
    else:
        time.sleep(1)