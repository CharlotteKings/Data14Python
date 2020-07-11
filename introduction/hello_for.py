#FOR LOOPS

# shopping_list = ['eggs', 'bacon', 'milk', 'bread']
# favourite_colour = ['blue', 'purple', 'red']
# for item in shopping_list:
#    for colour in favourite_colour:
#        print(colour, item)

# dict_data = {
#    1: {"name" : "alex" , "animal": "dog"},
#    2: {"name":"ben", "animal":"flamingo"},
#    3: {"name":"evie", "animal": "gorilla"},
#    4: {"name": "charlotte", "animal":"giraffe"}
# }

# for key in dict_data:                   # retrieve just one of them e.g name
#    print(dict_data[key]['name'])

# for key in dict_data:                       # retrieve all KYP
#    for inner_key in dict_data[key]:
#       print(dict_data[key][inner_key])

# for key in dict_data:
#    print(f"{dict_data[key]['name']}'s favourite animal is {dict_data[key]['animal']}")



# CHINESE MENU

chinese_menu = {
    101 :{ "dish" : "egg fried rice" , "price" : 1.60},
    102: { "dish" : "duck pancakes", "price": 7.40},
    103: { "dish" : "sweet and sour chicken", "price": 5.85}
}

for key in chinese_menu:
    print(f"I would like to buy {chinese_menu[key]['dish']} for £{chinese_menu[key]['price']:.2f}") # :.2f gives to 2dp

for key in chinese_menu:
    for inner_key in chinese_menu[key]:
        print(chinese_menu[key][inner_key])



