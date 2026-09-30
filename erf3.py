
contacts = []
while True:
    print('1 - add contact')
    print('2 - show contact')
    print('3 - edit contact')
    print('4 - remove contact')
    print('5 - exit')
    choice = input('Enter your choice:')
    match choice:
        case "1":
            code = input('Enter your code:')
            if any(code == contact[0] for contact in contacts):
                print('code is invalid')
            else:

                name = input('Enter your name:')
                phone = input('Enter your phone:')
                contacts.append([code , name , phone])
        case "2":
            if contacts:
                for contact in contacts:
                    print(f"code :{contact[0]} , name :{contact[1]} , phone :{contact[2]}")
            else:
                print('no contact')


        case "3":

            if contacts:
                for contact in contacts:
                    print(f"code :{contact[0]} , name :{contact[1]} , phone :{contact[2]}")
                code = input('Enter your code:')
                if any(code == contact[0] for contact in contacts):
                    new_name = input('Enter your name:')
                    new_phone = input('Enter your phone:')
                    contact[1]= new_name
                    contact[2]= new_phone
                    print('contact edited')
                else:
                    print('Invalid code')

            else:
                print('khalie ')

        case "4":
            if contacts:
                for contact in contacts:
                    print(f"code :{contact[0]} , name :{contact[1]} , phone :{contact[2]}")
                code = input('Enter your code:')
                if any(code == contact[0] for contact in contacts):
                    contacts.remove(contact)
                    print('contact removed')

        case "5":
            exit()





