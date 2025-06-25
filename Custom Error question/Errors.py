'''Write a code to generate a custom error so, when you put a string it will show an error custom message.'''
try:
    a = int(input("Enter a number for its square: "))
    print(f"Square of {a} is {a**2}")
except ValueError:
    raise ValueError("Invalid input. You must enter a number, not a string.")


