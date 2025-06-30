"""#1 WRITE A PYTHON PROGRAM TO DISPLAY A USER GOOD AFTERNOON AFTER ITS NAME TAKING INPUT FUNCTION."""

'''Name=str(input("Enter your name"))
print(f"Good Afternoon {Name}")'''

'''#2 Write a python program to fill this letter template given below
letter = """Dear <|NAME|>,
You are selected!
<|DATE|>"""'''

'''Name=str(input("Enter your name:"))
Date=input("Enter date")
print(f"""Dear <|{Name}|>,
You are selected!
<|{Date}|>""")'''

"""#3 write a python program to identify double spaces in string"""


'''text = input("Enter a string: ")
index = text.find("  ")
if index != -1:
    print(f"Double spaces found at index {index}.")
else:
    print("No double spaces found in the string.")'''


'''#4 Write a python program to replace double space string to single space string
text = input("Enter a string with double spaces: ")
new_text = text.replace("  ", " ")
print("String after replacing double spaces:")
print(new_text)'''

'''#5 Write a python program to format given letter using escape sequence character.
letter="Dear Harry, This python course is nice. Thanks!"'''
A=("Dear Harry,\n This python course is nice.\n Thanks!")
print(A)


