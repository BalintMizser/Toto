from data import kerdesek, eredmenyek

def menu():
    print('0 - kilépés')
    print('1 - ')
    return input("Válassz: ")

def readFromFile():
    file=open('eredmények.csv','r', encoding='utf-8')
    for row in file:
        data=row.strip().split(';')
        kerdesek.append(data[0])
        eredmenyek.append(data[1])
    file.close()

