products = []
total_price = 0

while True:
    name = input("Enter your product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    product = {"name": name, "quantity": quantity, "price": price}

    total_price += price
    if total_price <= 1000000 :

        print('done seccessfully')
        print(f"{product['name']} - {product['price']} - {product['quantity']}")
        products.append(product)

    else:
        print('price is more than 1000000')
        print('-'* 50)
        break
for product in products:
    print(f"{product['name']:10} - {product['price']:10} - {product['quantity']}")

