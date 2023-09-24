plate = input("Plate: ")
def main():
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(plate):
    if len(plate) > 6 or len(plate) < 2:
        return False
    if plate[0].isnumeric() or plate[1].isnumeric():
        return False
    if plate[2:].startswith("0"):
        return False
    for i in range (1,len(plate)-1):
        if plate[i].isdigit() and (plate[-1].isalpha() or plate[-2].isalpha()):
            return False
    for i in range(0,len(plate)):
        if not plate[i].isdigit() and not plate[i].isalpha():
            return False
    else:
        return True

main()