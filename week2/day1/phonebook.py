# copied the main menu from Canvas specifications 
mainMenu = "\nElectronic Phone Book \n ===================== \n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit \n \nWhat do you want to do (1-5)?"

# start with no content in the phone book, then fill it up with objects representing entries 
phoneBook = []

# I'm trying to work OOP into this... 
class Entry:
    def __init__(self, name, phoneNum):
        self.name = name 
        self.phoneNum = phoneNum

# main program function. I should probably split this up into more functions, but I don't see the point of doing so if each option can be achieved in 5 or fewer lines. 
def main():
    openBook = True     
    while openBook == True: # standard while loop. Broken by choice #5
        userChoice = input(mainMenu) # get the user input 

# 1. If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
        if userChoice == '1':
            lookUpName = input('Name:')
            for entry in phoneBook:
                if entry.name == lookUpName:
                    print(f'Found entry for {entry.name}: {entry.phoneNum}\n') 

# 2. If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
        if userChoice == '2':
            newName = input('Name:')
            newNum = input('Phone Number:')
            phoneBook.append(Entry(newName,newNum))
            print(f'Entry stored for {newName}.\n')

# 3. If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
        if userChoice == '3':
            deleteName = input('Name:')
            for entry in phoneBook:
                if entry.name == deleteName:
                    phoneBook.remove(entry) 
            print(f'Deleted entry for {deleteName}\n')

# 4. If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
        if userChoice == '4':
            for entry in phoneBook:
                print(f'Found entry for {entry.name}: {entry.phoneNum}\n')

# 5. If they choose to quit, end the program.
        if userChoice == '5':
            openBook = False
            print('Bye.') 

# start the main program 
main()