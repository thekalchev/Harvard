import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    is_random_font = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    is_random_font = False
else:
    print("Invalid usage")
    sys.exit(1)

# you can get a list of available fonts with code like this:
figlet.getFonts()

if is_random_font == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
     font=random.choice(figlet.getFonts())

message = input("Input: ")

print(f"Output:")
print(figlet.renderText(message))