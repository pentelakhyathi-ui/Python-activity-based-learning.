
def bill(units):
    if units < 0:
        return "Invalid"
    elif units <= 100:
        return units * 2 + 50
    elif units <= 200:
        return 100 * 2 + (units - 100) * 3 + 50
    else:
        return 100 * 2 + 100 * 3 + (units - 200) * 5 + 50

test_cases = [50, 80, 100, 150, 250]

for i in range(5):
    print("Test Case", i+1, ":", bill(test_cases[i]))
