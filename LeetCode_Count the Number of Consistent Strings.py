'''
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words.
 A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
'''

def countConsistentStrings(allowed: str, words: list[str]) -> int:
    ans = len(words)
    for item in words:
        for c in item:
            if c not in allowed:
                ans -= 1
                break
    return ans

if __name__ == "__main__":
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(countConsistentStrings(allowed, words))

    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(countConsistentStrings(allowed, words))


