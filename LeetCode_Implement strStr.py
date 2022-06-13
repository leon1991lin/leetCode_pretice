'''
28. Implement strStr()
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''


def strStr(haystack, needle):
    tmp = haystack.split(needle)
    if len(tmp) == 1:
        return -1
    else:
        return len(tmp[0])

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))

    haystack = "aaaaa"
    needle = "bba"
    print(strStr(haystack, needle))
