
def analyze(readings):
    average = sum(readings) / len(readings)

    if average <= 50:
        status = "Good"
    elif average <= 100:
        status = "Moderate"
    else:
        status = "Poor"

    return round(average, 2), max(readings), min(readings), status

test_cases = [
    [20, 30, 40],
    [40, 50, 60],
    [60, 80, 100],
    [120, 140, 160],
    [10, 20, 30]
]

for i in range(5):
    print("Test Case", i+1, ":", analyze(test_cases[i]))
