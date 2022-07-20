# a = input()
# b = a.split(" ")
# c = []
# for i in b:
#     c.append(int(i))
# print(max(c))
# print(min(c))

# a = input()
# b = a.split(" ")
# c = []
# for i in b:
#     c.append(int(i))
# d = sorted(c, reverse = True)
# e = ""
# for i in d:
#     e = e + str(i) + " "
# print(e)

# a = int(input())
# for i in range(a):
#     print(i+1)

# a = int(input())
# if a >= 60:
#     print("PASS")
# else:
#     print("FAIL")

# a = int(input())
# if a%2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

# a = int(input())
# if a >= 90:
#     print("A")
# elif a>= 80 and a<90:
#     print("B")
# elif a>= 70 and a<80:
#     print("C")
# elif a>= 60 and a<70:
#     print("D")
# else:
#     print("E")

# a = input()
# b = ""
# for i in a[-1::-1]:
#     b = b + i + " "
# print(b[:-1])
#
# a = input()
# print(len(a))

# a = input()
# b = ""
# for i in a[-1::-1]:
#     b = b + i
# print(int(b))

# a = input()
# b = map(int, a.split())
# print(max(b))


# b = input()
# c = map(int, b.split())
# print(sum(c))


# a = int(input())
# b = map(int, input().split())
# print(b)

# n = int(input())
# a = map(int, input().split())
# ans = ""
# for i in a:
#     if i >= 60:
#         ans = ans + "PASS" + " "
#     else:
#         ans = ans + "FAIL" + " "
# print(ans[:-1])
#
# n = int(input())
# a = input().split()
# ans = 0
# for i in a:
#     ans += int(i)
# print(ans)

# t = input()
# n = int(input())
# a = input().split()
# ans = ""
# for i in range(n):
#     if a[i] == t:
#         ans = ans + str(i+1) + " "
# print(ans[:-1])

# t = input()
# n = int(input())
# a = input().split()
# ans = ""
# for i in range(n):
#     if a[i] == t:
#         ans = ans + str(i+1)
# if ans == "":
#     print("0")
# else:
#     print(ans)

# t = input()
# a = input().split()
# ans = ""
# for i in range(len(a)):
#     if a[i] == t:
#         ans = ans + str(i+1) + " "
# print(ans[:-1])

# t = input()
# a = input().split()
# ans = 0
# for i in range(len(a)):
#     if a[i] == t:
#         ans = str(i)
#         break
# print(ans)

# t = input()
# n = int(input())
# a = input().split()
# ans = "0"
# for i in range(n):
#     if a[i] == t:
#         ans = str(i+1)
# print(ans)

# a = int(input())
# b = input().split()
# ans = 0
# for i in range(a):
#     ans += int(b[i])
# print(ans)

# a = input().split()
# t = input()
# ans = ""
# for i in range(len(a)):
#     if a[i] == t:
#         ans = ans + str(i+1) + " "
# print(ans[:-1])

# n = int(input("整數數量: "))
# a = input("input: ").split()
# m = int(input("要搜尋的數量: "))
# t = input("搜尋目標: ").split()
# f = 0 #已找到的數量
# ans = ""
# for i in range(n):
#     if a[i] in t:
#         ans = ans + str(i+1) + " "
#         f += 1
#     if f == m:
#         print(ans[:-1])
#         break

# a = input("input: ").split()
# t = input("搜尋目標: ").split()
# ans = ""
# for i in range(len(a)):
#     if a[i] in t:
#        ans = ans + str(i+1) + " "
# print(ans[:-1])

# a = input("input: ").split()
# t = int(input("target: "))
# ans = m_diff = float('inf')
# for num in a:
#     diff = abs(int(num)-t)
#     if diff < m_diff:
#         m_diff = diff
#         ans = int(num)
#     elif diff == m_diff and int(num) < ans:
#         ans = int(num)
# print(ans)

# a = input("input: ").split()
# t = int(input("target: "))
# ans = diff = float('inf')
# tmp = sorted([int(i) for i in a])
# diff = [abs(i-t) for i in tmp]
# print(tmp[diff.index(min(diff))])

# n = int(input("整數數量: "))
# a = input("input: ").split()
# m = int(input("要搜尋的數量: "))
# t = input("搜尋目標: ").split()
# ans = ""
# f = 0
# for ind in range(n):
#     print('item:',a[ind])
#     if a[ind] in t:
#         ans = ans + str(ind+1) + " "
#         print('ans:',ans)
#         f += 1
#         print("f:",f)
#         if f == m:
#             break

# t = int(input("搜尋目標: "))
# n = int(input("整數數量: "))
# a = [int(item) for item in input("input: ").split()]
# try:
#     print(a.index(t)+1)
# except ValueError:
#     print(0)

# n = input()
# if n == "":
#     n = 0
# a = input().split(" ")
# ans = 0
# for i in range(int(n)):
#     ans += int(a[i])
# print(ans)

# a = input()
# ans = 0
# for i in a:
#     if i != " ":
#         ans += int(i)
# print(ans)

# ans = []
# while True:
#     try:
#         a = int(input())
#         if a >= 60:
#             ans.append("PASS")
#         else:
#             ans.append("FAIL")
#     except:
#         break
# print("\n".join(ans))

# n = int(input())
# a = input().split(" ")
# ans = 0
# for i in a:
#     try:
#         if i != "" and i != " ":
#             ans += int(i)
#     except:
#         pass
# print(ans)

# n = int(input())
# a = map(int, input().split())
# ans = []
# for i in a:
#     if i >= 60:
#         ans.append("PASS")
#     else:
#         ans.append("FAIL")
# print(" ".join(ans))

# t = int(input())
# a = [int(item) for item in input().split()]
# try:
#     print(a.index(t)+1)
# except ValueError:
#     print(0)

# n = int(input())
# a = [int(item) for item in input().split()]
# ans = 0
# while n >= 1:
#     ans += a[n-1]
#     n -= 1
# print(ans)

# n = int(input())
# a = [int(item) for item in input().split()]
# m = int(input())
# t = [int(item) for item in input().split()]
# ans = []
# f = 0
# for ind in range(n):
#     if a[ind] in t:
#         ans.append(str(ind+1))
#         f += 1
#         if f == m:
#             break
# print(" ".join(ans))

# print(chr(36889),chr(26159))

"""
LeetCode 657. Robot Return to Origin

There is a robot starting at the position (0, 0), the origin, on a 2D plane.
 Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move.
Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once,
 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
"""

def judgeCircle(moves):
    tmp = {"R":1,"L":-1,"U":1,"D":-1}
    x, y = 0,0
    for c in moves:
        if c == "R" or c=="L":
            x += tmp[c]
        else:
            y += tmp[c]
    return x==y==0

'''
709. To Lower Case
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
'''
def toLowerCase(s: str):
    ans = ""
    for i in s:
        if ord(i) >= ord("A") and ord(i) <= ord("Z"):
            ans += chr(ord(i)+32)
        else:
            ans += i
    return ans

"""
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
def isPalindrome(s: str) -> bool:

    r = ""
    for c in s:
        if "A" <= c <= "Z":
            r += chr(ord(c)+32)
        elif "a" <= c <= "z" or "0" <= c <= "9":
            r += c

    for i in range(len(r)):
        if r[i] != r[-(i+1)]:
            return False

    return True
'''
520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
'''
# def detectCapitalUse(word) :
#     if word.islower() or word.isupper():
#         return True
#     elif word[0].isupper() and word[1:].islower():
#         return True
#     return False

def detectCapitalUse(word) :
    return word.islower() or word.isupper() or word.istitle()

# print(detectCapitalUse('Google'))

"""
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

def firstUniqChar(s: str):
    for i,c in enumerate(s):
        if s.count(c) == 1:
            return i
    return -1
# print(firstUniqChar("leetcode"))
# print(firstUniqChar("aabb"))

'''
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
'''

def defangIPaddr(address: str):
    return address.replace(".","[.]")

'''
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
def singleNumber(nums) -> int:
    for c in nums:
        if nums.count(c)==1:
            return c

nums = [4,1,2,1,2]
nums = [2,2,1]
# print(singleNumber(nums))

l = [3,7,5,5,7,3]
for i in range(len(l)):
    if l[i] == 5:
        print(i)
        break

