number = [12, 10, 7, 99, 67]

if len(number) > 1:
    result = [number[-1]] + number[:-1]
    print(result)
else :
    print(number)
