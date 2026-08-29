numbers = [0, 1, 0, 12, 3,0]

new_list = []

for number in numbers:
  if number != 0:
      new_list.append(number)

for i in range(numbers.count(0)):
    new_list.append(0)

print(new_list)


