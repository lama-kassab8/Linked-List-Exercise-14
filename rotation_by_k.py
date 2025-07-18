# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k ==0:
            return head
        current= head
        length= 1
        while current.next:
            current= current.next
            length +=1
        current.next= head
        new_tail_index= length - (k % length) -1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail= new_tail.next
        new_head= new_tail.next
        new_tail.next= None
        return new_head
        