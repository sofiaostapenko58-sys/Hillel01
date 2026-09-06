import string
letters = input("Enter a letters:")
parts = letters.split("-")
start = string.ascii_letters.index(parts[0])
end = string.ascii_letters.index(parts[1])
result = string.ascii_letters[start:end + 1]

print(result)