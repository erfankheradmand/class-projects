from unittest import case

books = []
users = []
borrows = []



while True:
    print('1 - add book')
    print('2 - show all books')
    print('3 - remove book')
    print('4 - edit book')
    print('5 - add new user(age > 18')
    print('6 - show users')
    print('7 - remove user')
    print('8 - edit user')
    print('9 - borrow a book ')
    print('10 - show all borrow books')
    print('0 - exit')

    print ('$' * 20 )



    choice = input('Enter your choice: ')

    match choice:
        case "1":
            book_code = input('Enter your book code: ')
            if any(book_code == book[0] for book in books ):
                print('book already used')
                print('$' * 20)

            else:
                book_name = input('Enter your book name: ')
                book_author = input('Enter your book author: ')
                books.append([book_code ,book_name, book_author])
                print('book added successfully')

                print('$' * 20)

        case "2":
            if books:
                for book in books:
                    print(f"book_code : {book[0]}, book_name : {book[1]}, book_author : {book[2]}")
                    print('$' * 20)
            else:
                print("book list empty")
                print('$' * 20)
        case "3":
            if books:
                for book in books:
                    print(f"book_code : {book[0]}, book_name : {book[1]}, book_author : {book[2]}")
                    print('$' * 20)
            else:
                print("book list empty")
                print('$' * 20)
                continue

            book_code = input('Enter your book code: ')

            found = False
            for book in books:
                if book_code == book[0]:
                    found = True
                    books.remove(book)
                    break
            if not found:
                print("book not found")
                print('$' * 20)

        case "4":
            if books:
                for book in books:
                    print(f"book_code : {book[0]}, book_name : {book[1]}, book_author : {book[2]}")

            else:
                print("book list empty")
                continue

            found = False

            book_code = input('Enter your book code: ')
            for book in books:
                if book_code == book[0]:
                    found = True
                    new_book_name = input('Enter your new book name: ')
                    new_book_author = input('Enter your new book author: ')
                    book[1] = new_book_name
                    book[2] = new_book_author
                    print('book edited successfully')
                    break
            if not found:
                print("book not found")

        case "5":
            user_code = input('Enter your user code: ')
            if any(user_code == user[0]for user in users):
                print('user already used')
            else:
                user_age = int(input('Enter your user age: '))
                if user_age < 18:
                    print('user not enough age')
                else:
                    user_name = input('Enter your user name: ')
                    users.append([user_code, user_name, user_age])
                    print('user added successfully')
        case "6":
            if users:
                for user in users:
                    print(f"user_code: {user[0]}, user_name: {user[1]}, user_age: {user[2]}")

            else:
                print("user list empty")

        case "7":
            if users:
                for user in users:
                    print(f"user_code: {user[0]}, user_name: {user[1]}, user_age: {user[2]}")
            else:
                print("user list empty")
                continue

            found = False
            user_code = input('Enter your user code: ')
            for user in users:
                if user_code == user[0]:
                    found = True
                    users.remove(user)
                    print('user removed successfully')
            if not found:
                print("user not found")

        case "8":
            if users:
                for user in users:
                    print(f"user_code: {user[0]}, user_name: {user[1]}, user_age: {user[2]}")
            else:
                print("user list empty")
                continue

            found = False
            user_code = input('Enter your user code: ')
            for user in users:
                if user_code == user[0]:
                    found = True
                    new_user_name = input('Enter your new user name: ')
                    new_user_age = int(input('Enter your new user age: '))

                    if new_user_age >=18:
                        user[1] = new_user_name
                        user[2] = new_user_age
                        print('user edited successfully')
                    else:
                        print("user not enough age")
                else:
                    print("user not found")
            if not found:
                print("user not found")

        case "9":
            if users:
                for user in users:
                    print(f"user_code: {user[0]}, user_name: {user[1]}")
            else:
                print("user list empty")
                continue
            user_code = input('Enter your user code: ')
            found = False
            for user in users:
                if user_code == user[0]:
                    user_found = True
                    if books:
                        for book in books:
                            print(f"book_code: {book[0]}, book_name: {book[1]}")
                    else:
                        print("book list empty")
                        continue
                    book_found = False
                    book_code = input('Enter your book code: ')
                    for book in books:
                        if book_code == book[0]:
                            book_found = True
                            borrows.append([user[0], user[1], book[0] , book[1]])
                            print("user borrow successfully")
                    if not book_found:
                        print("book not found")
            if not found :
                print("user not found")


        case "10":
            if borrows:
                for borrow in borrows:
                    print(f"user_code : {borrow[0]}, user_name : {borrow[1]},book_code :{borrow[2] }, book_name :{borrow[3]}")
            else:
                print("borrow list empty")
        case _:
            print("invalid input")

