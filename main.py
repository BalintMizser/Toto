from funcions import menu, readFromFile, kiir, beker, kereses, megoldas 
from data import kerdesek, eredmenyek
from os import system

import time
system('cls')
print('Készen áll?')
print('Ha igen nyomjon Entert!')
input()
choice= ''

while choice != '0':
    choice = menu()
    if choice == '1':
        readFromFile()
        #kiir()
        beker()
        time.sleep(1.5)
        system('cls')
        print('Feljegyezve!')
        time.sleep(2)
        system('cls')
        
    elif choice == '2':
        print(f'Találatok száma: {kereses()}\n')
        
    elif choice == '3':
        system('cls')
        print(f'{megoldas()}')
        time.sleep(2)
    elif choice == '0':
        time.sleep(1)
        system('cls')
        print('Viszlát!')
        time.sleep(1)
        system('cls')
        pass
    else:
        choice = ''
        print('Nincs ilyen opció!')
        time.sleep(1)