#hi


products = []
persons = []
cart = []


while True:
    print('1 -add product')
    print('2 -remove product')
    print('3 -edit product')
    print('4 -show all products')
    print('5 -add person')
    print('6 -remove person')
    print('7 -edit person')
    print('8 -show persons')
    print('9 - shop')
    print('10 -exit')
    choice = input('Enter your choice: ')

    match choice:
        case "1":
            product_code = input('Enter product code: ')
            if any (product_code == product[0] for product in products):
                print('Product code already exists')

            else:
                name = input('Enter product name: ')
                brand = input('Enter product brand: ')
                price = int(input('Enter product price: '))
                if price < 0  :
                    print('Invalid price')
                else:
                    count = int(input('Enter product count: '))
                    if count < 0 :
                        print('Invalid count')
                    else:
                        products.append([product_code, name, brand, price , count])
                        print('added product successfully')
        case "2":
            # if products:
            #     for product in products:
            #         print(f"product code: {product[0]}, name: {product[1]}, brand: {product[2]}, price: {product[3]} , count: {product[4]}")
            # else:
            #     print("No products")
            #     continue


            if products:
                found = False
                product_code = input('Enter product code: ')
                for product in products:

                    if product_code == product[0]:
                        found = True
                        products.remove(product)
                        print('removed product successfully')

                if not found:
                    print("product not found")
            else :
                print("product list is empty")

        case "3":
            # if products:
            #     for product in products:
            #         print(f"product code: {product[0]}, name: {product[1]}, brand: {product[2]}, price: {product[3]} , count: {product[4]}")
            # else:
            #     print("No products")
            #     continue

            if products:
                found = False
                product_code = input('Enter product code: ')
                for product in products:
                    if product[0] == product_code:
                        found = True

                        new_name = input('Enter new product name: ')
                        new_brand = input('Enter new product brand: ')
                        new_price = int(input('Enter new product price: '))
                        new_count = int(input('Enter new product count: '))
                        name = new_name
                        brand = new_brand
                        price = new_price
                        count = new_count
                        print('product edited ')
                if not found:
                    print("product not found")

            else:
                print("product list is empty")


        case "4":
            if products:
                for product in products:
                    print(f"product code: {product[0]}, name: {product[1]}, brand: {product[2]}, price: {product[3]} , count: {product[4]}")
            else:
                print("No products")


        case "5":
            person_code = input('Enter person code: ')
            if any(person_code== person[0] for person in persons ):
                print("person already exists")

            else:
                name = input('Enter person name: ')
                national_code = input('Enter person national code: ')
                if any(national_code== person[2] for person in persons ) :
                    print("person national code already exists")

                else:
                    age = int(input('Enter person age: '))
                    if age < 18 :
                        print('age should be more than 18')
                    else:
                        persons.append([person_code, name, national_code, age])
                        print('added person successfully')

        case "6":
            # if persons:
            #     for person in persons:
            #         print(f"person_code : {person[0]}, name : {person[1]},national_code : {person[2]}, age : {person[3]} ")
            # else:
            #     print("No persons")
            #     continue

            if persons:
                person_code = input('Enter person code: ')
                found = False
                for person in persons:
                    if person[0] == person_code:
                        found = True

                        persons.remove(person)
                        print('removed person successfully')
            if not found:
                print("person list is empty")
        case "7":
            # if persons:
            #     for person in persons:
            #         print(f"person_code : {person[0]}, name : {person[1]},national_code : {person[2]}, age : {person[3]} ")
            #     else:
            #         print("No persons")
            #         continue

            if persons:
                found = False
                person_code = input('Enter person code: ')
                for person in persons:
                    if person[0] == person_code:
                        found = True
                        new_name = input('Enter person name: ')
                        new_national_code = input('Enter person national code: ')
                        if any(new_national_code == person[2] for person in persons):
                            print("person national code already exists")

                        else:
                            new_age = int(input('Enter person age: '))
                            if new_age < 18:
                                print('age should be more than 18')
                            else:
                                name = new_name
                                national_code = new_national_code
                                age = new_age

                                print('person edited successfully')

        case "8":
            if persons:
                for person in persons:
                    print(f"person_code : {person[0]}, name : {person[1]},national_code : {person[2]}, age : {person[3]} ")
            else:
                print("No persons")


        case "9":
            if not persons:
                print("persons list is empty")
                continue
            if not products:
                print("product list is empty")
                continue

            for person in persons:
                print(f"person_code : {person[0]}, name : {person[1]},national_code : {person[2]}, age : {person[3]}")

            buyer = []
            while True:
                buyer_code = input('Enter buyer code: ')
                person_found = False
                for person in persons:
                    if person[0] == buyer_code:
                        buyer = person
                        person_found = True
                        break
                if person_found:
                    break
                print('buyer not found')
            while True:
                for product in products:
                    print(f"product code: {product[0]}, name: {product[1]}, brand: {product[2]}, price: {product[3]} , count: {product[4]}")
                while True:
                    product_code = input('Enter product code: ')
                    product_found = False
                    for product in products:
                        if product[0] == product_code:
                            product_found = True
                            break
                    if product_found:
                        break
                    print('product not found')
                while True:

                    product_count = int(input('Enter product count: '))

                    if product_count <= product[4]:
                        product[4] -= product_count
                        total_price = product_count * product[3]
                        cart.append([buyer[0], buyer[1], product[0] , product[1] , product_count, total_price])
                        break
                    print('this count is not available')
                answer = input('Do you want to add another product?(yes/no): ')
                if answer == 'no':
                    break
                final_price = 0
                for i in cart:
                    print(f"buyer : {i[1]} , product : {i[3]} , count : {i[4]},price : {i[5]}")
                    final_price += i[5]
                print(f"total price: {final_price}")
                chance = 3
                while chance > 0:
                    national_code = input('Enter national code: ')
                    if national_code == buyer[2]:
                        print('shopping complete')
                        cart.clear()
                        break
                    else :
                        chance -= 1
                        print('national code not found')
                        if chance > 0:
                            print('again')
                if chance == 0:
                    print('shopping failed')
                    cart.clear()






            # if persons:
            #     for person in persons:
            #         print(f"person_code : {person[0]}, name : {person[1]},national_code : {person[2]}, age : {person[3]} ")
            # else:
            #     print("No persons")
            #     continue
            #
            #
            #
            # while True:
            #     found = False
            #     person_code = input('Enter person code: ')
            #     for person in persons:
            #         if person[0] == person_code:
            #             found = True
            #             if products:
            #                 for product in products:
            #                     print(f"product code: {product[0]}, name: {product[1]}, brand: {product[2]}, price: {product[3]} , count: {product[4]}")
            #             else:
            #                 print("No products")
            #                 continue
            #             while True:
            #                 found = False
            #                 product_code = input('Enter product code: ')
            #                 for product in products:
            #                     if product[0] == product_code:
            #                         found = True
            #                         product_count = int(input('Enter product count: '))
            #                         if product_count <= product[4]:
            #                             product[4] -= product_count
            #                             answer = input('do you want to add another product?(yes/no): ')
            #                             if answer == 'yes':
            #                                 continue
            #                             else:
            #                                 buyer_code = person[0]
            #                                 buyer_name = person[1]
            #                                 product_code = product[0]
            #                                 product_name = product[1]
            #                                 total_price = product_count * product[3]
            #                                 cart.append([buyer_code, buyer_name, product_code, product_name,product_count,total_price])
            #                                 print(cart)
            #                                 chance = 3
            #                                 while chance > 0:
            #                                     f_national_code = input('Enter person national code again to check: ')
            #                                     if f_national_code == person[2]:
            #                                         print('shopping completed successfully')
            #                                         cart.clear()
            #                                         break
            #                                     else:
            #                                         chance -= 1
            #                                         print('shopping failed try again(3 - chance)')
            #                                 if chance == 0:
            #                                     print('shopping failed')
            #                                     cart.clear()
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #
            #                         else:
            #                             print('not enough product in stock')
            #                             continue
            #
            #                     else:
            #                         print("product not found try again")
            #                         continue
            #
            #
            #
            #
            #         else:
            #             print("person does not exist")
            #             continue












