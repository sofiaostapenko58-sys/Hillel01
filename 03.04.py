numbers = [0, 1, 7, 2, 4, 8]
if numbers == [] :
   print(0)

else :
   total = 0
   for i in range(0, len(numbers), 2):
      total = total + numbers[i]

print(total * numbers[-1])
