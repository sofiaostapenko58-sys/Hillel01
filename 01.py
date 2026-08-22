seconds = int(input("Enter seconds: "))
hours = None
hours = seconds // 3600
if seconds >= 60 :
    print ("More than a minute")
    if seconds >= 3600 :
        print ("More than a hour")
    seconds = seconds % 60
    hours = True
elif seconds == 0 :
    print ("Seconds is zero")
elif seconds < 0 :
    print ("Seconds is negative")
print ("Seconds: ", seconds)
print ("Hours:", hours)