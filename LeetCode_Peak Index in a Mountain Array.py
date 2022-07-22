'''
852. Peak Index in a Mountain Array

An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
'''
def peakIndexInMountainArray(arr: list[int]) -> int:
    l, r = 1 , len(arr)-2
    m = (l+r)//2

    while m != l:
        if arr[r] < arr[m]:
            if arr[m] < arr[m-1]:
                r = m
            else:
                l = m

        if arr[l] < arr[m]:
            if arr[m] < arr[m+1]:
                l = m
            else:
                r = m

        m = (l+r)//2

    if arr[r] > arr[m]:
        return r
    else:
        return m

    # return arr.index(max(arr))

if __name__ == "__main__":
    # arr = [0, 1, 2, 4, 5, 6, 7, 4, 3, 0]
    # print(peakIndexInMountainArray(arr))
    #
    # arr = [24,69,100,99,79,78,67,36,26,19]
    # print(peakIndexInMountainArray(arr))

    arr = [55,59,63,99,97,94,84,81,79,66,40,38,33,23,22,21,17,9,7]
    print(peakIndexInMountainArray(arr))