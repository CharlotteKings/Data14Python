# Function to check if inputted values are integers
def check(val):
    while not val.isnumeric():
        val = input("Please type a valid number? \n")
    if val.isnumeric:
        return int(val)

# Assign
counter = check(input("What number do you want to start from? \n"))
limit = check(input("What number do you want to finish at? \n"))
multiple1 = check(input("Choose the first number"))
Fizz = input(f"What would you like to say when the number is divisible by {multiple1}? \n")
multiple2 = check(input("Choose a second number"))
Buzz = input(f"What would you like to say when the number is divisible by {multiple2}? \n")

# FizzBuzz
for number in range(int(counter),int(limit),1):
    if number % multiple1 == 0 and number % multiple2 ==0:  # Change values for fizz and buzz
        print(f"{Fizz}{Buzz}")
    elif number % multiple1 == 0:
        print(f"{Fizz}")
    elif number % multiple2 ==0:
        print(f"{Buzz}")
    else:
        print(number)