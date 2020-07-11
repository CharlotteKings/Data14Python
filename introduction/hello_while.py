counter = 0

while counter < 10:
    print(f"Still counting {counter}")
    if counter == 6:
        break
    counter += 1
print("You've escaped the loop")

for number in range(10):
    print(number)

age = ""

while not age.isnumeric():
    age = input("Enter your age: \n")
    if age.isnumeric():
        age = int(age)
        break
    else:
        print("That is not a number, try again")

print(f"You are {age}")