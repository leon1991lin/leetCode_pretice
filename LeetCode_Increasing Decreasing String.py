'''
1370. Increasing Decreasing String

You are given a string s. Reorder the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
'''
def sortString(s: str) -> str:
    count = {}
    for c in s:
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1
    result = ""
    while sum(count.values()) > 0:

        for n in sorted(count.keys()):
            if count[n] > 0:
                result += n
                count[n] -= 1

        for n in sorted(count, reverse=True):
            if count[n] > 0:
                result += n
                count[n] -= 1

    return result


if __name__ == "__main__":
    s = "aaaabbbbcccc"
    print(sortString(s))

    s = "rat"
    print(sortString(s))


