# 234. Palindrome Linked List

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True