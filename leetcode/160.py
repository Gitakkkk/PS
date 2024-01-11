# 160. Intersection of Two Linked Lists

# 내가 작성한 코드
# Hash 사용 (정석적인 투 포인터로 해결한 방법이 아님)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        _set = set()
        node = headA
        while node:
            _set.add(node)
            node = node.next
        
        node = headB
        while node:
            if node in _set: return node
            node = node.next

        return None

# 다른 사람이 작성한 코드
# 투 포인터를 사용하여 해결

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptrA, ptrB = headA, headB
        while ptrA != ptrB:
            if ptrA != None:
                ptrA = ptrA.next
            else:
                ptrA = headB
            if ptrB != None:
                ptrB = ptrB.next
            else:
                ptrB = headA
        return ptrA