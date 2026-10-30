
def compress(s):
    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1

    result += s[-1] + str(count)

    if len(result) >= len(s):
        return s
    return result

test_cases = [
    "aaabbc",
    "xxxxxy",
    "aabbcc",
    "hhhhhhhh",
    "abcdef"
]

for i in range(5):
    print("Test Case", i+1, ":", compress(test_cases[i]))
