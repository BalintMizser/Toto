from funcions import menu, readFromFile
choice= ''
while choice != '0':
    choice = menu()
    if choice == '1':
        readFromFile()