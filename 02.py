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

