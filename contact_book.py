
def main():
    monkey = True
    while(monkey == True):
        print("View the contact list in full by typing VIEW." + "\n")
        print("If you would like to ADD a contact, type ADD." + "\n")
        print("If you would like to FIND a contact, type FIND." + "\n")
        print("If you would like to delete or edit an contact, please use FIND to first search for the contact." + "\n")
        print("Type X to quit" + "\n")
        answer = input()
        if answer == "X":
            break
        elif answer == "ADD":
            writing()
        elif answer == "VIEW":
            print()
            view()
        elif answer == "FIND":
            contact = input("Who are you searching for?" + "\n")
            line_num = find(contact)
            if line_num == -1:
                print("This contact does not exist." + "\n")
            else:
                choice = input("If you would like to delete or edit this contact, type D or E. Otherwise, click enter to continue." + "\n")
                if choice == "D":
                    delete(line_num)
                elif choice == "E":
                    edit(line_num)
            
        
    

def writing():
    new_contact = input("Please write the name of the contact" + "\n")
    num_contact = input("Please add the number of this person." + "\n")
    contact = new_contact + " " + num_contact
    with open('contacts.txt', 'a') as file:
            
        file.write(contact + "\n")
        file.flush()

def view():
    with open('contacts.txt', 'r') as file:
        for line in file:
            print(line)
    
    input("Press enter to continue")
  
def edit(line_num):

    new_contact = input("Please write the name of the contact" + "\n")
    num_contact = input("Please add the number of this person." + "\n")
    contact = new_contact + " " + num_contact

    with open('contacts.txt', 'r') as file:
        temp = file.readlines()

        temp[line_num] = contact + "\n"
        

    with open("contacts.txt", 'w') as file:
        file.writelines(temp)
        file.flush()        
    
    
def find(name): 
    counter = 1

    with open('contacts.txt', 'r') as file:
        temp = file.readlines()

        for line in temp:
            if line.__contains__(name):
                print(line)
                return counter
            counter + 1
    return -1    
          
    
def delete(num):
    
    with open('contacts.txt', 'r') as file:
        temp = file.readlines()
        del temp[num]
        for line in temp:
            print(line)
    
    with open("contacts.txt", 'w') as file:
          file.writelines(temp)
          file.flush()




if __name__ == "__main__":
    main()