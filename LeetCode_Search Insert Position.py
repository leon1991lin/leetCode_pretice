'''
35. Search Insert Position

Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

def searchInsert(nums, target):

    if nums[-1] < target:
        return len(nums)

    elif nums[0] > target:
        return 0

    else:
        for i in range(len(nums)):

            if nums[i] == target:
                return i

            elif nums[i] < target and nums[i+1] > target:
                return i+1


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    print(searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 2
    print(searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 7
    print(searchInsert(nums, target))

    nums = [1]
    target = 1
    print(searchInsert(nums, target))