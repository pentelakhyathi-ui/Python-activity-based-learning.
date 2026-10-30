
def validate(p):
    upper = lower = digit = special = False

    for ch in p:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if len(p) >= 8 and upper and lower and digit and special and "password" not in p.lower():
        return "Valid Password"
    return "Invalid Password"

test_cases = [
    "Hello@123",
    "python123",
    "HELLO@123",
    "Hi@12",
    "Password@123"
]

for i in range(5):
    print("Test Case", i+1, ":", validate(test_cases[i]))
