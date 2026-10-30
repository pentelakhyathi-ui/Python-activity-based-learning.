
def sentiment(text):
    positive = ["good", "excellent", "helpful", "nice"]
    negative = ["bad", "poor", "difficult", "worst"]

    score = 0

    for word in text.lower().split():
        if word in positive:
            score += 1
        elif word in negative:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"

test_cases = [
    "good excellent",
    "bad poor",
    "helpful nice",
    "good bad",
    "difficult worst"
]

for i in range(5):
    print("Test Case", i+1, ":", sentiment(test_cases[i]))
