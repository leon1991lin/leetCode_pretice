'''
69. Sqrt(x)
Given a non-negative integer x,
compute and return the square root of x.

Since the return type is an integer,
the decimal digits are truncated,
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator,
such as pow(x, 0.5) or x ** 0.5.
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        else:
            h, l = x, 2
            while l <= h:
                mid = (h + l)//2
                if mid*mid == x:
                    return mid
                elif mid*mid > x:
                    h = mid-1
                else:
                    l = mid+1
            return l-1

#binary search

if __name__ == "__main__":
    x = 8
    print(Solution().mySqrt(x))

    x = 9
    print(Solution().mySqrt(x))

    x = 170
    print(Solution().mySqrt(x))

    x = 226
    print(Solution().mySqrt(x))




