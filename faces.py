def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string
def main():
    string = input("Enter a string: ")
    print(convert(string))

main()