from decimal import *

worths_and_names = {
    5000: "£50 note(s)", 2000: "£20 note(s)", 1000: "£10 note(s)", 500: "£5 note(s)", 200: "£2 coin(s)",
    100: "£1 coin(s)", 50: "50p coin(s)", 20: "20p coin(s)", 10: "10p coin(s)", 5: "5p coin(s)",
    2: "2p coin(s)", 1: "1p coin(s)"
}

def question():
    moneyinput = input("Input an amount of money and I will show you the denominations of currency in £GBP that make up"
                       " that sum. (Or type 'quit' to exit.)" + "\n")

    if moneyinput.lower() in ["quit", "exit"]:
        return False
    else:
        try:
            moneyinput = Decimal(moneyinput) * 100
        except InvalidOperation:
            print("That seemed like an invalid input. Try again.")
            return True
        if moneyinput != int(moneyinput):
            print("Invalid. Did you input too many decimal places? Try again.")
            return True

    #FOR DEBUGGING
    #print(moneyinput)

    while moneyinput > 0:
        for key, value in worths_and_names.items():
            currencyamount, moneyinput = divmod(moneyinput, key)
            if currencyamount > 0:
                print("{} {}".format(int(currencyamount), value))

    return True

while question():
    pass
