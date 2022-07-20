'''
2011. Final Value of Variable After Performing Operations

There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
'''


def finalValueAfterOperations(operations: list[str]) -> int:
    ans = 0
    for c in operations:
        if "+" in c:
            ans += 1
        else:
            ans -= 1
    return ans



if __name__ == "__main__":
    operations = ["--X","X++","X++"]
    print(finalValueAfterOperations(operations))