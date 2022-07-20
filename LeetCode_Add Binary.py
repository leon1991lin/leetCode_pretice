'''
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a,2)+int(b,2))
        return str(sum[2:])


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a,b))

    a = "11"
    b = "1"
    print(Solution().addBinary(a,b))


