'''
53. Maximum Subarray

Given an integer array nums,
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''

def maxSubArray(nums):
    maxSum = currentSum = nums[0]
    for num in nums[1:]:
        currentSum = max(currentSum+num, num)
        maxSum = max(maxSum,currentSum)
    return maxSum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))

    nums = [1]
    print(maxSubArray(nums))

    nums = [5, 4, -1, 7, 8]
    print(maxSubArray(nums))