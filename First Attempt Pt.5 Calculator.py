print("Issa Calculator")
print("Let's do some numbers")
num_1 = input("Enter the first Number:")
num_2 = input("Enter the other Number:")
operation = input("What do you wanna do with this?")

result = eval(str(num_1) + operation + str(num_2))

print(result)