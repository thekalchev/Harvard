import inflect #github test
p = inflect.engine()
names = []
while True:
    try:
        name = input("Name: ")
        if name not in names:
            names.append(name)
    except EOFError:
        mylist = p.join((names))
        print("Adieu, adieu, to ", end="")
        print(mylist)
        exit()
