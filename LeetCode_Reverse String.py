'''
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''

def reverseString(s: list[str]) -> None:

    # for i in range(-2,(-len(s)-1),-1):
    #     print(i)
    #     s.append(s.pop(i))
    #
    # return None

    s[:] = s[::-1]

    return None



if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(s)
    print(s[:])
    print(s[::-1])
    reverseString(s)
    print(s)

    s = ["H", "a", "n", "n", "a", "h"]
    reverseString(s)

    print(s)
