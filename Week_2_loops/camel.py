camel_str = input("camel:  ")

snake_str = '' #empty string to store the value of the snake case version
for i in range(len(camel_str)): #iterates through every letter if the input
    if camel_str[i].isupper() and i != 0: #if the word is upper and it is not the first letter
        snake_str += '_' + camel_str[i].lower()
    else:
        snake_str += camel_str[i].lower()

print(snake_str)