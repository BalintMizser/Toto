from data import kerdesek, eredmenyek, tippek
from os import system
meccsek=''

def menu():
    print('0 - kilépés')
    print('1 - ')
    return input("Válassz: ")

def readFromFile():
    system('cls')
    file=open('eredmenyek.csv','r', encoding='utf-8')
    for row in file:
        data=row.strip().split(';')
        kerdesek.append(data[0])
        eredmenyek.append(data[1])
    file.close()

def kiir():
    system('cls')
    for k,e in zip(kerdesek,eredmenyek):
        print(f'{k}: {e}')
    input()

def beker():
    system('cls')
    for i in range(len(kerdesek)):
        tippek.append(input(f'{kerdesek[i]}:'))
    # print(tippek)
    input()