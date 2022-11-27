from data import kerdesek, eredmenyek, tippek
from os import system
import time

meccsek=''

def menu():
    print('0 - kilépés')
    print('1 - tippelj! (1,2,x)')
    print("2 - kiértékelés")
    print('3 - nyereményem')
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
    time.sleep(0.5)
    # input()
    
def kereses():
    talalt = 0
    for tipp, eredmeny in zip(tippek, eredmenyek):
        if tipp==eredmeny:
            talalt += 1
    return talalt

def megoldas():
    szoveg= ''
    talalt2=10
    if kereses()==talalt2:
        print('Nyereményed 20.000 Ft')
    elif kereses()==11:
        print('Nyereményed 100.000 Ft')
    elif kereses()==12:
        print('Nyereményed 625.000 Ft')
    elif kereses()==13:
        print('Nyereményed 1.000.000 Ft')
    elif kereses()==14:
        print('Nyereményed 5.000.000 Ft')
    else:
        kereses()<talalt2
        print('Sajnáljuk nem nyertél!')
    return szoveg
            
    
