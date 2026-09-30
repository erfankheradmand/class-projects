contacts = []
while True:
    print('1 - add new contact')
    print('2 - show all contacts')
    print('3 - edit contact')
    print('4 - remove contact')
    print('5 - exit')

    choice = input('Enter your choice: ')
    match choice:
        case  "1":
            code = input('Enter your code: ')
            if any(code == contact[0] for contact in contacts):
                print('Contact already exists')
            else:
                name = input('Enter your name: ')
                phone = input('Enter your phone number: ')
                contacts.append([code , name , phone ])
                print('Contact added')

        case "2":
            if contacts:
                for contact in contacts:
                    print (f"code : {contacts[0]} , name : {contacts[1]} , phone : {contacts[2]}")

            else :
                print('no contact added')

        case "3":
            if contacts:
                for contact in contacts:
                    print(f"code : {contacts[0]} , name : {contacts[1]} , phone : {contacts[2]}")

            else:
                print('no contact added')
                continue
            code =input('Enter your code: ')

            found = False
            for contact in contacts:
                if code == contact[0]:
                    found = True
                    new_name = input('Enter your name: ')
                    new_phone = input('Enter your phone number: ')
                    contact[1] = new_name
                    contact[2] = new_phone
                    print('Contact edited successfully')
                    break
            if not found:
                print('code not found')

        case "4":
            if contacts:
                for contact in contacts:
                    print(f"code : {contact[0]} , name : {contact[1]} , phone : {contact[2]}")
            else:
                print('no contact added')
                continue

            code =input('Enter your code: ')
            found = False
            for contact in contacts:
                if code == contact[0]:
                    found = True
                    contacts.remove(contact)
                    print('remove success')
                    break

            if not found:
                print('code not found')

        case "5":
            exit()

        case _ :
            print('Invalid code')








