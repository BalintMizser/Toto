from funcions import menu, readFromFile, kiir, beker,kereses
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
        menu()
    elif choice == '2':
        print(f'Találatok száma: {kereses()}')
    elif choice == '3':
        print('')
    elif choice == '0':
        pass
    else:
        choice = ''
        print('Nincs ilyen opció!')
        time.sleep(1)