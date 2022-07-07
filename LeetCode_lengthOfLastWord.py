'''
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split()
        return len(tmp[-1])

if __name__ == "__main__":
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))

    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s))

    s = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s))

