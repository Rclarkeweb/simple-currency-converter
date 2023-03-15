# Currency Coverter
print("Hello, welcome to the console exchange rate")

# Ask user for their name
username = input("What is your name? ")
print("Hello ", username)

# Ask user to choose a currency
print("We have the following exhange rates for you: USD, EUR, JPY")
chosencurrency = input("What currency do you want to convert GBP to? ")
chosencurrency = chosencurrency.upper()

# Check that input currency is accepted
if chosencurrency == "USD":
    print("You have chosen:", chosencurrency)
elif chosencurrency == "EUR":
    print("You have chosen:", chosencurrency)
elif chosencurrency == "JPY":
    print("You have chosen:", chosencurrency)
else:
    print("Hmm, you didn't enter an accepted currency. Please refresh and try again")
    
# Ask the user for the amount they want to convert
gbpamount = input("How much money do you want to convert? ")
gbpamount = float(gbpamount)
gbpamount = round(gbpamount, 2)
print(f'You want to convert £ {gbpamount:.2f} to {chosencurrency}')

# Convert the users amount to the chosen currency
if chosencurrency == "USD":
    usdamount = gbpamount * 1.20
    print(f'You would get ${usdamount:.2f}')
elif chosencurrency == "EUR":
    euramount = gbpamount * 1.14
    print(f'You would get €{euramount:.2f}')
elif chosencurrency == "JPY":
    jpyamount = gbpamount * 159.39
    print(f'You would get ¥{jpyamount:.2f}')
else:
    print("Oops something went wrong. Please refresh.")
