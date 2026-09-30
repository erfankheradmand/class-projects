# # # # # """
# # # # # start
# # # # # born --->input
# # # # # age = 2026 - born
# # # # # IF (age < 13) do
# # # # #      'kooodak'--->output
# # # # # ELIF(19>age>=13)
# # # # #      'nojavan'--->output
# # # # # ELIF(30>age>=19)
# # # # #      'lavan'--->output
# # # # # ELIF(60>age>=30)
# # # # #      'bozorgsal'--->output
# # # # # ELIF(age>=60)
# # # # #      'salmand'--->output
# # # # # ELSE
# # # # # """
# # # # # """
# # # # # start
# # # # # num---> input
# # # # # IF (num%2==0)do
# # # # #     'even'---->output
# # # # # ELSE do
# # # # #     'odd'---->output
# # # # # end IF
# # # # #
# # # # # """
# # # # # num = int(input("Enter a number: "))
# # # # # if num%2==0:
# # # # #     print('even')
# # # # # else:
# # # # #     print('odd')
# # # # """
# # # # start
# # # # num<---input
# # # # IF (num%2==0)do
# # # #     'even'--->output
# # # # ELSE do
# # # #     'odd'--->output
# # # # ENDIF
# # # # end
# # # # """
# # # # """
# # # # start
# # # # num<---input
# # # # IF(num>0)do
# # # #     '+'--->output
# # # # ELIF(num<0)do
# # # #     '-'--->output
# # # # ELSE do
# # # #     '0'--->output
# # # # ENDIF
# # # # END
# # # # """
# # # # num = int(input('adad bede: '))
# # # # if num > 0 :
# # # #     print('+')
# # # # elif num < 0 :
# # # #     print('-')
# # # # else :
# # # #     print('0')
# # # """
# # # start
# # # (num1,num2,op)<---input
# # # IF (op=='+') do
# # #     (num1+num2)---->output
# # # ELIF (op=='-') do
# # #     (num1-num2)---->output
# # # ELIF (op=='*') do
# # #     (num1*num2)---->output
# # # ELIF (op=='/') do
# # #     IF num2==0 do
# # #         'eroor'--->output
# # #     ELSE do
# # #         (num1/num2)---->output
# # #
# # # """
# # # num1 = int(input('enter first number: '))
# # # num2 = int(input('enter second number: '))
# # # op = input('enter operation: ')
# # # if op == '+':
# # #     print(num1+num2)
# # # elif op == '-':
# # #     print(num1-num2)
# # # elif op == '*':
# # #     print(num1*num2)
# # # elif op == '/':
# # #     if num2 == 0:
# # #         print('eror')
# # #     else:
# # #         print(num1/num2)
# # # else:
# # #     print('eroooor')
# #
# #
# # """
# # mach case
# # condition ---->variable(key)/ == ---> match case (switch case )---> 3.10
# # case 's':
# #     print('up')
# # case 's':
# #     print('down')
# # #else
# # case _ :
# #     print('up')
# # case '_':
# #     print('invalid')
# # """
# #
# #
# #
# # # """
# # # start
# # # number<---input
# # # i = 0
# # # mul = 1
# # # while i<number do
# # #     i ++
# # #     mul *= i
# # #     mul--->output
# # # ENDWHILE
# # # end
# # number = int(input('number: '))
# # i = 1
# # mul = 1
# # while i < number:
# #     i += 1
# #     mul *= i
# # print(mul)
# #
# #
# #
# # #1 -use case diagram
# # #2 - class diagram
# # #3 - entity diagram
# #
# #
# from turtledemo.penrose import start
#
# from unicodedata import digit
#
# # start
# # number--->input
# # n_number = 0
# # WHILE number>0 do
# #     digit = number % 10
# #     n_number += 1
# #     number // 10
# # n_number ----->output
# # end
#
# #
# # number = int(input("Enter a number: "))
# # n_number = 0
# # while number > 0:
# #     n_number += 1
# #     number //=10
# # print (n_number)
#
# #start
# #number ---->input
# #even_number = 0
# #odd_number = 0
# #WHILE number > 0 do
#     #digit = number % 10
#     #IF digit % 2 ==0 d0
#         #even_number+=1
#     #ELSE do
#         #odd_number += 0
#     #number //= 10
#     #ENDIF
# #ENDWHILE
# # output
# #end
# #
# # number = int(input("Enter a number: "))
# # even_number = 0
# # odd_number = 0
# # while(number > 0):
# #     digit = number % 10
# #     if digit % 2 == 0:
# #         even_number += 1
# #     else:
# #         odd_number += 1
# #     number //= 10
# # print ('even number:' ,even_number)
# # print ('odd number:' ,odd_number)
#
# n1 = int(input('N1:'))
# n2 = int(input('N2:'))
# sm = 0
# while n1 < n2:
#     if n1 % 2 != 0:
#         sm += n1
#         n1 += 1
#         print(sm)
#
#
# #
# #
# num = int(input(' adad bede :'))
# a = 1
#
# while a < num:
#     a = a + 1
#     if a % 3==0 and a %    5==0:
#         print (num)
# number = int(input('bede :'))
# sm = 0
# i = 0
# while i <= number:
#     sm += i
#     i += 1
# print(sm)
# number = 143859381
# while number > 0:
#     digit = number % 10
#     print(digit)
#     number //= 10
#     print(number)
#     print(50 * '*')
# number = int(input())
# max_digit = 0
# while number > 0:
#     digit = number % 10
#     if digit > max_digit:
#         max_digit = digit
#     number //= 10
# print (max_digit)



"""
1 - start
2- number ---> input
3- mul = 1
4 - for i set 1 ; i < number ; i ++
    5 - mul *= i
6 - ENDFOR
7 - mul --->output
8 - END
"""
from random import choice

# number = int(input(" adadbede :"))
# mul = 1
# for i in range(1,number+1):
#     mul *= i
# print(mul)



"""
1 - start 
2- number ---> input
3 - For i set 1 ; i < number + 1 ; i ++
    4 - if number % i == 0 do
        5- i ---> output
    6 - ENDIF
7 - ENDFOR
8 - END
"""
# number = int(input('inter number : '))
# for i in range(1, number+1):
#     if number % i == 0:
#         print(i)
"""
1 - start 
2- n = 100
3 - sm = 0
4 - For i set 0 ; n <= 100 ; i +=2
    5 - sm += i 
6 - ENDFOR
7 - END
"""
# n = 100
# sm = 0
# for i in range(0 , n + 1 , 2):
#     sm += i
# print(sm)


"""
1- start 
2- a , b = 0 , 1
3-
4 - For i set 0 ; i < 10 ; i ++
    5- a ----> output
    6 - a , b = b , a + b
7 - ENDFOR
8 - END 
"""
#
# a , b = 0 , 1
# for i in range(0,10):
#     print (a)
#     a , b = b , a + b
#
# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4   :
#             print("*" , end= " ")
#         else :
#             print(" " , end= " ")
#     print()
# n = int(input('adad'))
# fac = 1
# for i in range (1 , n+1):
#     fac *= i
# print(fac)
# for i in range(10,0,-2):
#     print(i)
# for i in range(5):
#     for j in range(5 - i):
#         print('*' , end =' ')
#     print()
# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[4 ])
# a = [1,2,3,4,5,6]
# b = [4,5,6,7,8,9]
# common = []
# for i in a:
#     if i in b:
#         common.append(i)
# # print(common)
# n = [ 2,3,34,5,65,7676,232,4]
# print(n[ :  : -1])




# # سوپر مهم
# contacts = []
# while True:
#     print('1 - add contacts ')
#     print('2 - show all contacts ')
#     print('3 - edit  contact ')
#     print('4 - remove  contact ')
#     print('0 - exit ')
#     print ('$' * 20)
#     choice = input('Enter your choice: ')
#     print('$' * 20)
#
#
#     match choice:
#         case "1":
#             code = input('Enter your contact code: ')
#             if any(code == contact[0] for contact in contacts):
#                 print('code used ')
#                 print('$' * 20)
#             else:
#                 name = input('Enter your contact name: ')
#                 PHONE = input('Enter your contact phone number: ')
#
#                 contacts.append([code , name , PHONE ])
#
#                 print('code added ')
#
#                 print('$' * 20)
        #
        #
        # case "2":
        #     if contacts:
        #         for contact in contacts:
        #             print(f"code : {contact[0]}, name : {contact[1]}, phone : {contact[2]}")
        #
        #     else:
        #         print("no contacts ")
        #         print('$' * 20)
        #
        # case "3":
        #     if contacts:
        #         for contact in contacts:
        #             print(f"code : {contact[0]}, name : {contact[1]}, phone : {contact[2]}")
        #
        #     else:
        #         print("no contacts ")
        #         print('$' * 20)
        #
        #     continue

            code = input('Enter your contact code:')
            found = False

            for contact in contacts:
                if contact[0] == code:
                    found = True

                    new_name = input('Enter your contact name:')
                    new_phone = input('Enter your contact phone number:')

                    contact[1] = new_name
                    contact[2] = new_phone

                    print('change successfuly')
                    print('$' * 20)
                    break

            if not found:
                print("no contacts ")
                print('$' * 20)

# 20        case "4":
#             if contacts:
#                 for contact in contacts:
#                     print(f"code : {contact[0]}, name : {contact[1]}, phone : {contact[2]}")
#
#             else:
#                 print("no contacts ")
#                 print('$' * 20)
#
#             code = int('Enter your contact code: ')
#             found = False
#
#             for contact in contacts:
#                 if contact[0] == code:
#                     found = True
#
#                     contacts.remove(contact)
#
#                     print('remove successfuly')
#
#                     print('$' * 20)
#                     break
#             if not found:
#                 print("no contacts ")
#                 print('$' * 20)
#
#         case "0":
#             exit()
#
#         case _:
#             print('invalid input')
#             print('$' * 20)



contacts = []

while True:
    print(' welcome ')
    print('1 - add contacts ')
    print('2 - show all contacts ')
    print('3 - edit  contact ')
    print('4 - remove  contact ')
    print('5 -searching contacts ')
    print('0 - exit ')
    choice = input('Enter your choice: ')

    match choice:
        case "1":
            code = input('Enter your contact code: ')
            if any(code == contact[0] for contact in contacts):
                print('code used ')
                print('=' * 20)
            else:
                name  = input('Enter your contact name: ')
                phone = input('Enter your contact phone number: ')
                contacts.append([code , name  , phone ])
                print('add successful')
                print('=' * 80)


        case "2":
            if contacts:
                for contact in contacts:
                    print(f"code : {contact[0]}, name : {contact[1]}, phone : {contact[2]}" )
                    print('=' * 20)

            else:
                print("no contacts ")
        case "3":
            if contacts:
                for contact in contacts:
                    print(f"code : {contact[0]}, name : {contact[1]}, phone : {contact[2]}")
                continue

                print('=' * 20)
                code = input('Enter your contact code: ')
                if code == contact[0]:
                    new_name = input('Enter your contact name:')
                    new_phone = input('Enter your contact phone number:')
                    contact[1] = new_name
                    contact[2] = new_phone
                else:
                    print("no contacts ")
            else:

                print("no contacts ")







