students = ["DAVID", "lee", "RICHARD"]

result = filter(str.isupper,students)
# Anything filter is True keep
# Anything filter is False delete

print(list(result))
number = list(range(1,100))

def even_divisible(num):
    return num % 2 == 0 and num % 3 ==0


print(list(filter(even_divisible,number)))