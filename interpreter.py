
expression = input("Enter an arithmetic expression (in the format 'x y z'): ")

x, y, z = expression.split()


x = int(x)
z = int(z)


if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
else:
    print("Invalid operator")
    exit()

print("{:.1f}".format(result))