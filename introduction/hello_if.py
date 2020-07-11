#CONTROL FLOW

# age =int(input("How old are you? \n"))
# if age > 18:                                    # need a boolean answer here (True or False)
#    print("You can see the scary film")
# elif age == 18:
#    print("You are only just old enough")
# else:
#    print("You are too young")

# print('Everybody can be here')


film_rating  = '15'
if film_rating == '18':
    print("Must be over 18 to watch")
elif film_rating == '15':
    print('Must be over 15 to watch')
elif film_rating == '12A' or film_rating == '12':
    print('Must be over 12 to watch')
elif film_rating == 'PG':
    print('Please watch with an adult')
elif film_rating == 'U':
    print('Suitable for everyone')
else:
    print('Enter a valid film rating')







