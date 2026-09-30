#library management
from exam3 import book_code

books = []
users = []
borrows = []
while True:
    print('1-add a book')
    print('2-show all books')
    print('3- remove a book')
    print('4- edit a book')
    print('5- add  new user')
    print('6- show all users')
    print('7- remove a user')
    print('8- edit a user')
    print('9- borrow a book')
    print('10- show all borrows')
    print('11- exit')
    choice = input('Enter your choice: ')
    print('&' * 20)




    match choice:
        case "1":
            book_code = input("Enter your book code: ")
            if any(book_code == book[0] for book in books):
                print("book already exist")
            else :
                book_name = input("Enter your book name: ")
                book_author = input("Enter book author: ")
                books.append([book_code, book_name, book_author])


        case "2":
            if books:
                for book in books:
                    print(f"book_code: {book[0]}, book_name: {book[1]}, book_author: {book[2]}")

                    print('&' * 20)

                else:
                    print("book list empty")

                    print('&' * 20)

        case "3":
            for book in books:
                print(f"")




