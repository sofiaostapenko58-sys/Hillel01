numbers = [1, 2, 3, 4, 5]

if len(numbers) % 2 == 0:
    middle = len(numbers) // 2
else :
   middle = len(numbers) // 2 + 1

result = [numbers[:middle] ,numbers[middle:]]
print(result)
