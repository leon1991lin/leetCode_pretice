'''
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have.
Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''
def numJewelsInStones(jewels: str, stones: str) -> int:
    ans = 0
    for c in stones:
        if c in jewels:
            ans += 1
    return ans

if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels, stones))