first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))

action = input ("Enter(+,*,-,/) :")
if action == "+":
    print(first_number + second_number)
elif action == "-":
    print(first_number - second_number)
elif action == "*":
    print(first_number * second_number)
elif action == "/":
    if second_number != 0:
     print(first_number / second_number)
    else :
     print('Second number cannot be zero')