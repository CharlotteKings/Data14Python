# data14 = ["Katie", "Juxhen", "Joe"]
#
# # Map applies a function to an iterable
#
# data14_capitalised = map(str.upper,data14)
#
# # Map is lazy so force as list
# print(list(data14_capitalised))
# print(type(data14_capitalised))


# Write a function that squares a number and adds 3
numbers = [1,2,3,4,5]
numbers2 = [10,100,1000]  # One list longer than other = output ends at the end of shortest input

def square_add(num, add):
        return num * num + add

num_map = map(square_add,numbers, numbers2)  # can map a function with 2 inputs

print(list(num_map))