'''
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list,
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

'''
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        curr = head
        before = curr
        after = curr.next
        while after:
            if before.val == after.val:
                before.next = after.next
                after = after.next
            else:
                before = after
                after = after.next
        return curr

if __name__ == "__main__":
    head = [1,1,2]
    print(Solution().deleteDuplicates(head))

    head = [1,1,2,3,3]
    print(Solution().deleteDuplicates(head))

