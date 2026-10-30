
def ranking(candidates):
    eligible = []

    for name, marks, assessment, attendance in candidates:
        if marks >= 60 and assessment >= 50 and attendance >= 75:
            total = marks + assessment + attendance
            eligible.append((name, total))

    eligible.sort(key=lambda x: (-x[1], x[0]))
    return eligible

test_cases = [
    [("A", 80, 70, 90)],
    [("B", 55, 80, 90)],
    [("C", 90, 85, 95)],
    [("D", 70, 60, 80), ("E", 85, 75, 90)],
    [("F", 80, 40, 90)]
]

for i in range(5):
    print("Test Case", i+1, ":", ranking(test_cases[i]))
