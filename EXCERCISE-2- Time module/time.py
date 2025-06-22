import time
t= time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)

if hour >=0 and hour < 12:
    print("Good Morning!")
elif hour >=12 and hour <= 17:
    print("Good Afternoon!")
else:
    print("Good Evening!")

''' Create a python program capable of greeting you with Good morning, Good afternoon and Good evening. your program should use time module to get the current hour .'''