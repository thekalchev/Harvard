def task(str, dots):
    return dots.join(str.split())
str = input()
dots = "..."
print(task(str,dots))