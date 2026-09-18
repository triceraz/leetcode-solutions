# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            return head
        prev = head
        cur = head.next
        head.next = None
        while cur.next is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        cur.next = prev
        return cur
