'''
1704. Determine if String Halves Are Alike

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
'''

def halvesAreAlike(s: str) -> bool:
    # s = s.lower()
    # m = len(s)//2
    # a, b = s[:m], s[m:]
    # vowels =  ['a', 'e', 'i', 'o', 'u']
    # for v in vowels:
    #     tmp = 0
    #     for ac, bc in zip(a,b):
    #         if ac == v:
    #             tmp += 1
    #         elif bc == v:
    #             tmp -= 1
    #     if tmp != 0:
    #         return False
    # return True
    s = s.lower()
    m = len(s)//2
    a, b = s[:m], s[m:]
    vowels =  ['a', 'e', 'i', 'o', 'u']
    tmp = 0
    for ac, bc in zip(a,b):
        if ac in vowels:
            tmp += 1
        if bc in vowels:
            tmp -= 1
    if tmp == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    s = "book"
    print(halvesAreAlike(s))

    s = "textbook"
    print(halvesAreAlike(s))