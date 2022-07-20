'''
1221. Split a String in Balanced Strings
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
'''


def balancedStringSplit(s: str) -> int:
    ans, num = 0, 0
    for c in s:
        if c == "R":
            num += 1
        else:
            num -= 1
        if num == 0:
            ans += 1
    return ans

if __name__ == "__main__":
    s = "RLRRLLRLRL"
    print(balancedStringSplit(s))

    s = "RLRRRLLRLL"
    print(balancedStringSplit(s))

    s = "LLLLRRRR"
    print(balancedStringSplit(s))