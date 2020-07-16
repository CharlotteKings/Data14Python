# # Open creates a 'file stream'

#
# try:
#     print("Trying to open file...")
#     file = open("order.txt")
#     print("Succesfully opened file...")
# except #FileNotFoundError:  # specify error - shouild do this
#     print("Error!")

# Will run try first and will run as much of
# it as it can until it hits an error
# If can't completer move on to execpt
# Can have multipe except blocks


# Error messages can be useful in telling us whats wrong
# Heres how to see the error message without the crash
# try:
#     print("Trying to open file...")
#     file = open("order.txt")
#     print("Succesfully opened file...")
# except FileNotFoundError as errmsg:  # specify error - shouild do this
#     print(errmsg)


# Add finally
# try:
#     print("Trying to open file...")
#     file = open("order.txt")
#     print("Succesfully opened file...")
# except FileNotFoundError as errmsg:  # specify error - shouild do this
#     print(errmsg)
# finally:
#     print("Finished")


# OPENING FILES
# r = read mode (default)
# w = write mode (if no file, creates one; if file, truncate)
# x = create mode
# a = append mode (if no file, creates one; if file, appends)
# t = text mode
# b = binary mode
# + = reading and writing

# USING IT IN A FUNCTION
# def open_and_print_file(filename):
#     try:
#         opened_file = open(filename,"r")
#         file_line_list = opened_file.readlines()
#
#         for line in file_line_list:
#             print(line.rstrip('\n'))  # Normally prints with extra lines between lines, rstrip stops this
#
#         #opened_file.close()
#
#     except FileNotFoundError:
#         print("File not found")
#         raise

# open_and_print_file("order.txt")

# DIFFERENCE BETWEEN READLINE AND READLINES
# READLINE - reads line and moves on to next, read line is gone
# READLINES - reads all lines, all lines then gone

# WITH
# with open("order.txt") as opened_file:
#     print(opened_file.readlines())

# FUNCTION WITH 'WITH' CLAUSE
# def open_and_print_file(filename):
#     try:
#         with open(filename, "r") as opened_file:
#             file_line_list = opened_file.readlines()
#
#             for line in file_line_list:
#                 print(line.rstrip('\n'))  # Normally prints with extra lines between lines, rstrip stops this
#
#     except FileNotFoundError:
#         print("File not found")
#         raise
#
# open_and_print_file("order.txt")

# with open("order.txt", "w") as opened_file:
#     opened_file.write("Cheeseburger")
#

def write_file(filename,order):
    try:
        with open(filename, "w") as opened_file:
            opened_file.write(order)

    except FileNotFoundError:
        print("File not found")
        raise

#write_file("order.txt","pasta")

def append_file(filename,order):
    try:
        with open(filename, "a") as opened_file:
            opened_file.write(order +'\n')

    except TypeError:
        print("Oops. Please put a string")

append_file("order.txt","HotDog")
append_file("order.txt",5)







