'''
1662. Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''

def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    word1, word2 = ''.join(word1), ''.join(word2)
    return word1==word2

if __name__ == "__main__":
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(arrayStringsAreEqual(word1, word2))

    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(arrayStringsAreEqual(word1, word2))