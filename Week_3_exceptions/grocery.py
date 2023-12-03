groceries = {}
while True:
    try:
        product = input()
        if product not in groceries:
            groceries[product] = 1
        else:
            groceries[product] += 1
    except EOFError:
        break

for product in sorted(groceries):
    count = groceries[product]
    print(f"{count} {product.upper()}")