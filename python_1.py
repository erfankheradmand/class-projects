tool = float(input('Enter product count(meghdar tool ro vared konid): '))
arz  = float(input('Enter product count(meghdar arz ra vared konid)): '))

area = arz * tool
print( "masahat : " , area)

if 0 < area <= 100:
    print('mojavez nemikhad ')
elif 100< area <=200:
    print('bayad mojavez begirad ')
elif 200< area:
    print('mojavez shamel nemishe  ')
else:
    print('invalid input (adad eshtebah gofte shod )')
