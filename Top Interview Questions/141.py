# 141. Linked List Cycle

# fast 포인터는 두 칸씩 이동하고 slow 포인터는 한 칸씩 이동
# fast 포인터가 slow 포인터를 만나면 순회하므로 True, None을 만나면 False
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        # fast와 fast.next가 None이 아닌 동안 반복
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast: return True
        return False 