
def calendar(start, days):
    print("Mon Tue Wed Thu Fri Sat Sun")

    day = 1
    print("    " * start, end="")

    for i in range(days):
        print("%3d" % day, end=" ")

        if (start + day) % 7 == 0:
            print()

        day += 1

    print()

test_cases = [
    (0, 28),
    (1, 30),
    (2, 31),
    (3, 30),
    (6, 31)
]

for i in range(5):
    print("Test Case", i+1)
    calendar(test_cases[i][0], test_cases[i][1])
