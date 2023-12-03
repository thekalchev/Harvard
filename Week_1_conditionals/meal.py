def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes/60

def main():
    time = input("Enter the time in 24-hour format (HH:MM): ")
    decimal_time = convert(time)

    if 7 <= decimal_time <= 8:
        print("breakfast time")
    elif 12 <= decimal_time <= 13:
        print("lunch time")
    elif 18 <= decimal_time <= 19:
        print("dinner time")
    else:
        pass

if __name__ == "__main__":
    main()