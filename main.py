from funcions import menu, readFromFile, kiir, beker,kereses
from data import kerdesek, eredmenyek
from os import system

import time
choice= ''
system=('cls')
while choice != '0':
    choice = menu()
    if choice == '1':
        readFromFile()
        #kiir()
        beker()
    if choice == '2':
        print(f'Találatok száma: {kereses()}')
    if choice == '3':
        print('')
    else:
        choice=''
        time.sleep(1)