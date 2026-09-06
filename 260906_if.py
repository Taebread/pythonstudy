# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 18:
#         print("Plese pay $7")
#     elif age > 18:
#         print("You can ride the rollercoaster")
#     else:
#         print("please pay $12")
# else:
#     print("sorry you have to grow taller before you cna ride.")
#
# #Modulo Operator 모듈려 연산자 : 나머지를 구하는거
# # 10 % 5 = 0   10 % 3 = 1


print("Welcome to Python Piza Deliveries!")
size = input("What size pizza do you want? S, M or L")
pepperoni = input("Do you want pepperoni on you pizza? Y or N")
extra_cheese = input("do you want extra cheese? Y or N")

price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L" :
    price += 25
else:
    print("Sorry, please enter S, M, or L")

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3


if extra_cheese == "Y":
    price += 1

print(f"Your final bill is : {price}")