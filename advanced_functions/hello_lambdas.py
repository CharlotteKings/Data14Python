# Anonymous functions
#
# def add(n1,n2):
#     return n1 + n2
#
# print(add(2,2))
#
# add_lambda = lambda n1, n2: n1 +n2
# print(add_lambda(2,2))
#
# numbers = [101, 2843, 2, 283, 3]
# result = map(lambda x: x*x +3,numbers)
# print(list(result))

savings = [234.00, 555.00, 674.00, 78.00]
# bonus = list(map(lambda x: x * 1.1, savings))
# print(bonus)

even_savings = list(filter(lambda x: x % 2 ==0 , savings))
print(even_savings)
