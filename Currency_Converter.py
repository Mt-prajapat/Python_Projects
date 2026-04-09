from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://v6.exchangerate-api.com/v6"
API_KEY = "772e70f895c657bf7a817bad"

printer = PrettyPrinter()


def get_currencies():
    url = f"{BASE_URL}/{API_KEY}/codes"
    data = get(url).json()

    if data['result'] != 'success':
        print("Error fetching currencies")
        return []

    return data['supported_codes']


def print_currencies(currencies):
    for currency in currencies:
        print(f"{currency[0]} - {currency[1]}")


def exchange_rate(currency1, currency2):
    url = f"{BASE_URL}/{API_KEY}/pair/{currency1}/{currency2}"
    data = get(url).json()

    if data['result'] != 'success':
        print("Invalid currencies.")
        return None

    rate = data['conversion_rate']
    print(f"{currency1} -> {currency2} = {rate}")

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


main()