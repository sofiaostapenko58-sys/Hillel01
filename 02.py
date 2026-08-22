<<<<<<< HEAD
age = input("Please enter your age: ")
if not age.isdigit() or int(age) < 0 :
    print("Wrong input. Age cannot be negative.")
elif 0< int (age) < 10 :
    print("Milk")
elif 10<= int (age) < 18 :
    print("Caffe")
elif 18 <= int (age) < 60 :
    print("Beer")
elif 60 <= int (age) < 100 :
    print("Tea")
else :
    print("Wrong input. Age cannot be greater than 100.")
=======
number = int(input ('Enter a number:'))
print(number * number)

number1 = int(input ('Enter the first number: '))
number2 = int(input ('Enter the second number: '))
number3 = int(input ('Enter the third number: '))
print((number1 + number2 + number3 )/3)

minutes = int(input('Enter the number of minutes: '))
hours = minutes // 60
remaining_minutes = minutes % 60
print(hours,'hours', remaining_minutes, 'minutes')

price = int(input('Enter the price: '))
discount = int(input('Enter the discount(%): '))
discount_amount = price * discount / 100
final_price = price - discount_amount
print(final_price)

number = int(input('Enter a number: '))
last_digit = number % 10
print(last_digit)

length = int(input('Enter the length of the rectangle: '))
width = int(input('Enter the width of the rectangle: '))
perimeter = (length + width) * 2
print(perimeter)

number = int(input('Enter a four-digit number: '))
first = number // 1000
second = (number // 100) % 10
third = (number // 10) % 10
fourth = number % 10
print(first)
print(second)
print(third)
print(fourth)
>>>>>>> 5cca200e64405456283e69089c42791d007bf253
