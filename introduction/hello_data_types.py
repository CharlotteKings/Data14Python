# Numbers
# String
# Boolean

#a = 5
#b = 17
#c = 12
#print(a >= b)
#print(c != a) # not equal to
#print(a == b) # is equal to
#print(b % a)

# Numbers
# int, float, complex
# a = 5       # int
# b = 2.5     # float
# c = 3 +2j   # complex
# print(type(a))

# Strings
# single = 'Single quotes'
# double = "Double quotes"

# print(single, double)   #Both work the same but you must pick one!

# single_inside = 'i\'m using single quotes'  # Backslash to 'escape'
# print(single_inside)

# hw = "Hello world!"
# print(hw[4])    # print spectfic character in string    #Python starts counting at zero
# print(hw[3:7])  # characters from 3, up to but not including 7
# print(hw[4:])   # characters from 4, and the rest of the string
# print(hw[:8])   # all characters up tp but not including 8
# print(hw[-2])   # second from last character

# STRING METHODS AND FUNCTIONS
# white_space = '       Here is a string with a load of white space    '
# print(len(white_space))     #len is a function
# print(white_space.strip())  # get rid of white space    #.<method> is a method
# print(len(white_space.strip()))
# print(white_space.lstrip())     # left strip
# print(white_space.lstrip())     # right strip
# print(white_space.count("a"))     # count
# print(white_space.lower())      # all lower case
# print(white_space.upper())      # all upper case
# print(white_space.capitalize())     # capitalise
# print(white_space.replace('e','oooo'))  # replace e with oooo
# can layer these
# print(white_space.strip().capitalize().replace('e','oooo').count('o'))

# CONCATENATE
# a = 'ant'
# b = 'bear'
# c = 'cat'
# d = 5
# print(a + ', ' + b + ', ' + c)    #
# print(a + ', ' + b + ', ' + c + ', ' + str(d)) # cannot concatentise numbers, must make them a string
# print(f"{a}, {b}, {c}, {d}")    # f string does essentially the same thing but is not concatenation
# print(f"Hello, I am an {a}!")

#NAME, AGE, NUM OF SIBLINGS, FAV DECIMAL, FAV ANIMAL
# name = input("What is your name? \n")
# age = int(input("How old are you? \n"))
# siblings = input("How many siblings do you have? \n")
# decimal = float(input("What is your favourite decimal? \n"))
# animal = input("What is your favourite animal? \n")
# print(f"Hello {name}, you are {age} years old and have {siblings} siblings. Your favourite decimal is {decimal} and your favourite animal is a {animal}.")


#BOOLEAN
# a = True
# b = False

# print(a == b)
# print(a != b)
# print(a > b)

# print(True and True)
# print(True and False)
# print(True or False)

hw = "Hello World!"

print(hw.isalpha())     # Alphabetic characters only (no spaces)
print(hw.isalnum())     # alphabetic and numbers (no spaces)
print(hw.islower())     # All letters are lower case
print(hw.isupper())     # All letters are upper case
print(hw.endswith("!"))     # checks  what the string ends in
print(hw.startswith("h"))      #checks with what the string starts with

n = None    # similar to null in SQL, None is None = True and None == None is True, everything else is False

