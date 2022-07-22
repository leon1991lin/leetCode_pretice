'''
2315. Count Asterisks

You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.
'''
def countAsterisks(s: str) -> int:
    bar, count = 0, 0
    for c in s:
        if c == "|":
            bar += 1
        if bar%2 == 0:
            if c == "*":
                count += 1
    return count


if __name__ == "__main__":
    s = "l|*e*et|c**o|*de|"
    print(countAsterisks(s))

    s = "iamprogrammer"
    print(countAsterisks(s))

    s = "yo|uar|e**|b|e***au|tifu|l"
    print(countAsterisks(s))