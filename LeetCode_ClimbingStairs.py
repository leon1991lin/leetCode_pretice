'''
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
[1,2,3,5]
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        tmp = [1,2,3]
        if n <=3:
            return n
        else:
            for i in range(3,n):
                tmp.append(tmp[i-1]+tmp[i-2])
        return tmp[-1]

if __name__ == "__main__":
    n = 4
    print(Solution().climbStairs(n))