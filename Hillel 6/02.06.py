seconds = int(input("Enter seconds: "))

days = seconds // 86400
remainder = seconds % 86400

hours = remainder // 3600
remainder = remainder % 3600

minutes = remainder // 60
seconds = remainder % 60

if days % 10 == 1 and days != 11:
    word = "день"
elif days % 10 in (2, 3, 4) and days not in (12, 13, 14):
    word = "дня"
else:
    word = "дней"

print(days, word + ",", str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))


