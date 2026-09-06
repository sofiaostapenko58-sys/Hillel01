import string
import keyword

name = input("Enter your name: ")
valid = True

if name == "" or name[0].isdigit() or "__" in name:
    valid = False

for char in name:
    if char.isupper():
        valid = False

for char in name:
    if char in string.punctuation and char != "_":
        valid = False

for char in name:
    if char == " ":
        valid = False

if name in keyword.kwlist:
    valid = False

print(valid)