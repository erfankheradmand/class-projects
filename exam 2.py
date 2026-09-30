from unittest import case

books = []
users = []
borrows = []

while True:
    print('1 - add book')
    print('2 - show all books')
    print('3 - remove book')
    print('4 - edit book')
    print('5 - add new user')
    print('6 - show users')
    print('7 - remove user')
    print('8 - edit user')
    print('9 - borrow a book ')
    print('10 - show all borrow books')
    print('0 - exit')


    choice = input('Enter your choice: ')

    match choice:
        case "1":
            book_code = input('Enter your book code: ')
            if any(book_code == book[0] for book in books ):
                print('book already used')

            else:
                book_name = input('Enter your book name: ')
                book_author = input('Enter your book author: ')
                books.append([book_code ,book_name, book_author])
                print('book added')

        case "2":
            if books:
                for book in books:
                    print(f"book_code : {book[0]}, book_name : {book[1]}, book_author : {book[2]}")

            else:
                print("book list empty")

        case "3":
            if books:
                for book in books:
                    print(f"book_code : {book[0]}, book_name : {book[1]}, book_author : {book[2]}")

            else:
                print("book list empty")
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
                user_name = input('Enter your user name: ')
                user_age = int(input('Enter your user age: '))
                if user_age >= 18:
                    users.append([user_code, user_name, user_age])

                    print('user added successfully')

                else:
                    print("age not allowed")

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
            if books:
                for book in books:
                    print(f"book_code: {book[0]}, book_name: {book[1]}, book_author : {book[2]}")
            else:
                print("book list empty")
                continue
            book_code = input('Enter your book code: ')
            found = False
            for book in books:
                if book_code == book[0]:
                    book_found = True
                    if users:
                        for user in users:
                            print(f"user_code: {user[0]}, user_name: {user[1]}, user_age: {user[2]}")
                    else:
                        print("user list empty")
                        continue
                    user_found = False
                    user_code = input('Enter your user code: ')
                    for user in users:
                        if user_code == user[0]:
                            user_found = True
                            borrows.append([book[0], book[1], user[0] , user[1]])
                            print("user borrow successfully")
                    if not user_found:
                        print("user not found")
            if not found :
                print("book not found")


        case "10":
            if borrows:
                for borrow in borrows:
                    print(f"book_code : {borrow[0]}, book_name : {borrow[1]},user_code :{borrow[2] }, user_name :{borrow[3]}")
            else:
                print("borrow list empty")
        case _:
            print("invalid input")