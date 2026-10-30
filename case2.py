
def atm(transactions):
    balance = 5000

    for action, amount in transactions:
        if amount <= 0:
            continue
        elif action == "deposit":
            balance += amount
        elif action == "withdraw":
            if amount <= 3000 and amount <= balance:
                balance -= amount

    return balance

test_cases = [
    [("deposit", 1000)],
    [("withdraw", 2000)],
    [("deposit", 1000), ("withdraw", 500)],
    [("withdraw", 4000)],
    [("withdraw", 6000)]
]

for i in range(5):
    print("Test Case", i+1, ":", atm(test_cases[i]))
