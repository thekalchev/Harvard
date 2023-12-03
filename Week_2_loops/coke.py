person_amount = 0
coke = 50
while person_amount <50:
    print("Amount Due: ", coke - person_amount)
    input_coin = int(input("Insert Coin: "))
    if input_coin not in [5,10,25]:
        input_coin = 0
    person_amount += input_coin
print("Change Owed: ", person_amount - coke)