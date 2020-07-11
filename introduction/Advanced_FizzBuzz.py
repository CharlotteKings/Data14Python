counter = int(input("What number do you want to start from? \n"))   # Accept user input for number to start from?
limit = int(input("What number do you want to finish at? \n"))      # Accept user input for number to count up to
Fizz = input("What would you like to say when the number is divisible by 3? \n")    # Accept user input for custom fizz buzz?
Buzz = input("What would you like to say when the number is divisible by 5? \n")
while counter < limit:
    counter += 2                                        # Change the number we increment by
    if counter % 4 == 0 and counter % 5 ==0:            # Change values for fizz and buzz
        print(f"{Fizz}{Buzz}")
    elif counter % 4 == 0:
        print(f"{Fizz}")
    elif counter % 5 ==0:
        print(f"{Buzz}")
    else:
        print(counter)