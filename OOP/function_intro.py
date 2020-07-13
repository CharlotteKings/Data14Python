# Don't
# Repeat
# Yourself

# DEF 1
# def print_something():  # Needs () and :
#    print("Something!")

# print_something()

# DEF 2
# def print_something_multiple(something, number_of_times):  # Function with arguements
#    string_to_print = something * number_of_times
#    print(string_to_print)

# print_something_multiple("Woohoo!", 3)

# DEF 3
# def repeat_string(string_to_repeat, number_of_repeats=3):  # How to default, must be at the end
#    string_to_return = string_to_repeat * number_of_repeats
#    return string_to_return


# print(repeat_string("Woohoo!"))

# DEF 4
# def addition(num1,num2):
#    return num1 + num2


# print(addition(9,6))

# DEF 5
# Given a tuple of numbers
# Set up a current product tracker
# Iterate through each number
# Multiply current product by number
# Return the number

# DEF 6
#def find_product(*multiargs):
#    product = 1
#    for num in multiargs:
#        product = product * num
#    return product

#print(find_product(1, 2, 3, 4))

# DEF 7
# Assigning types to inputs
# PRO: Eases reading
# CON: Increases amount you have to write
def repeat_string(string_to_repeat: str, number_of_repeats: int = 3) -> str:  # Assign types to inputs can still have defult values as shown
    string_to_return = string_to_repeat * number_of_repeats
    return string_to_return

print(repeat_string("hello"))