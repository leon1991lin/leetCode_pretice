'''66. Plus One

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = str(int("".join([str(i) for i in digits])) + 1)
        ans = [ int(i) for i in num]
        return ans

if __name__ == "__main__":
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))

    digits = [9]
    print(Solution().plusOne(digits))