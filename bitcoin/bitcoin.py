import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif not sys.argv[1].isdigit():
    sys.exit("Command-line argument is not a number")
else:

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_object = json.loads(response.text)
        current_bitcoin_price_usd = bitcoin_object['bpi']['USD']['rate_float']
        total_bitcoin_cost = float(sys.argv[1]) * current_bitcoin_price_usd
        print(f"${total_bitcoin_cost:,.4f}")

    except requests.RequestException:
        sys.exit("Request error!")