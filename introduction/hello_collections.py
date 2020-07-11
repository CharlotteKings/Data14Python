# lists (aka array)

shopping_list = ['eggs', 'bread', 'cheese', 'sausages']
#print(type(shopping_list))
#print(shopping_list[3])

#shopping_list.append('mushrooms')   # add something
#shopping_list.remove('cheese')      # remove something

# pop_return = shopping_list.pop()    #removes last element in list    #modifies list and returns something
# print(shopping_list.pop())

# TUPLES - imputable cannot change them (only 2 methods - count and index)
# colours = ('blue', 'purple', 'turquoise')

# print(colours[-1])
# print(colours.count('blue'))    #count how many times blue appears in tuple
# print(colours.index('purple'))  # where item appears in tuple

# DICTIONARIES
# my_dict = {"key": "value"}  #key value pairs
# print(my_dict)
# print(type(my_dict))

# bigger_dictionary = {
#   "name" : "Charlotte"
#    ,"age" : 20
#    , "favourite animal" : "Giraffe"
# }
# print(bigger_dictionary['age'])     # Find value connected to key - must be name of key

# bigger_dictionary['favourite colour'] = 'purple'        # Add new KVP

# del bigger_dictionary['age']        # delete KVP

# print(bigger_dictionary)
# No order, interchangeable order
# cannot find a key from value as values aren't unique but keys are

# print(bigger_dictionary.keys())     #list all keys
# print(bigger_dictionary.values())     #list all values

data14_dictionary = {
    'Trainer' : 'David',
    'Number of participants' : 11,
    'Name of participant' : ['Charlotte', 'Jade' ],
}

print(data14_dictionary['Name of participant'][0])      # return specific value in a KVP list

#SETS - lists with no order

car_parts = {'wheels', 'battery', 'doors'}
car_parts.add('pedals')     # add to set
car_parts.discard('wheels')         # delete from set
print(car_parts)

#FROZEN SET

fs = frozenset([1,2,3,4])
print(fs)