import sys
import requests

# get value from command-line
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print('Command-line argument is not a number')
        sys.exit(1)
# get current price of Bitcoin as a float e print with the value of the command-line
else:
    print('Missing command-line argument')
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bitcoin = (response['bpi']['USD']['rate_float'])
    amount = bitcoin * value
    print(f'${amount:,.4f}')
except requests.RequestException:
    print('RequestException')
    sys.exit(1)