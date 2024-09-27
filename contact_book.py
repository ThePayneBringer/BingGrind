
def main():
    monkey = True
    while(monkey == True):
        print("Would you like to ADD, SEARCH, EDIT, or DELETE a contact?" + "\n")
        print("Type X to quit" + "\n")
        answer = input()
        if answer == "X":
            break
        elif answer == "ADD":
            writing()
        elif answer == "EDIT":
            edit()
        elif answer == "SEARCH":
            search()
        elif answer == "DELETE":
            delete()
        else:
            print("Please input a valid answer" + "\n")

        
    

def writing():
    new_contact = input("Please write the name of the contact" + "\n")
    num_contact = input("Please add the number of this person." + "\n")
    contact = new_contact + num_contact
    file = open('Contacts', 'a')
    file.write(contact + "\n")
    file.flush()
    

def edit():
    with open('Contacts', 'r') as file:
        temp = file.readlines()
    
    print(temp)
    line = input("Which line number would you like to change?" + "\n" + "\n")
    line_num = int(line)
    contact_name = input("Please record the newly editted contact" + "\n" + "\n")
    temp[line_num] = contact_name + "\n"
    
    with open('Contacts', 'w') as file:
        file.writelines(temp)

def search():
    contact = input("Who are you searching for?" + "\n")
    with open('Contacts', 'r') as file:
        temp = file.readlines()
    for line in temp:
        if contact in line:
            print(line)
    
    
    
def delete():
    counter = 1
    contact = input("Which contact are you deleting?" + "\n")
    with open('Contacts', 'r') as file:
        temp = file.readlines()
    for line in temp:
        if contact in line:
            with open('Contacts', 'w') as file:
                file.writelines(temp)
                break
        counter+1
    
if __name__ == "__main__":
    main()