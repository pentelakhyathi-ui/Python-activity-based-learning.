
def evaluate(answers):
    key = ["A", "B", "C", "D", "A"]
    correct = wrong = unanswered = 0

    for a, k in zip(answers, key):
        if a == "":
            unanswered += 1
        elif a == k:
            correct += 1
        else:
            wrong += 1

    score = correct * 2 - wrong * 0.5
    return correct, wrong, unanswered, score

test_cases = [
    ["A", "B", "C", "D", "A"],
    ["A", "B", "C", "A", "B"],
    ["", "", "", "", ""],
    ["A", "C", "C", "D", "A"],
    ["B", "B", "", "D", "C"]
]

for i in range(5):
    print("Test Case", i+1, ":", evaluate(test_cases[i]))
