'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
'''


def lengthOfLongestSubstring(s: str) -> int:
    max = 0
    for i in range(len(s)):
        tmp = s[i]
        for c in s[i+1:]:
            if c not in list(tmp):
                tmp += c
            else:
                break
        if len(tmp) > max:
            max = len(tmp)
    return max

if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(lengthOfLongestSubstring(s))