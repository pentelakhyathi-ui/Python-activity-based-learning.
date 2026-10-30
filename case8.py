
def eligibility(attendance, lab, internal, fees):
    if attendance < 75:
        return "Not Eligible"
    elif lab < 80:
        return "Not Eligible"
    elif internal < 40:
        return "Not Eligible"
    elif fees != "paid":
        return "Not Eligible"
    else:
        return "Eligible"

test_cases = [
    (80, 90, 50, "paid"),
    (60, 90, 50, "paid"),
    (80, 60, 50, "paid"),
    (80, 90, 30, "paid"),
    (80, 90, 50, "unpaid")
]

for i in range(5):
    print("Test Case", i+1, ":", eligibility(*test_cases[i]))
