# 1 - #start
# 2 - #number_1,number_2,op <--- input
# 3 - #IF (op =='+') do
#     4 - sm = number_1+number_2
#     5 - sm ---> output
# 6 - else if (opp=='-') do
#     7- minus = number_1-number2
#     8-minus --> output
# 9- else if (op =="*") do
#     10 - mul= number_1 * number_2
#     11 - mul ---> output
# 12 - else if (op == "/") do
#     13 - IF (number_2==0)do
#         14 - 'second number cant be 0'
#     15 - else do
#         16- dev = number_1/ number_2
#         17 - div-->output
#     18_ENDIF
# 19- ELSE do:
#     20-'invalid operator'---->output
# 21- ENFIF
# 22- end



number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))
op = input("Enter operation:(+,-,*,/)")


if op == "+":
    sm  = number_1 + number_2
    print(sm)
elif op == "-":
    minus = number_1 - number_2
    print(minus)
elif op == "*":
    mul = number_1 * number_2
    print(mul)
elif op == "/":
    if number_2!=0:
        div = number_1 / number_2
        print(div)
    else:
        print('second number is zero')
else:
    print('Invalid operation')

