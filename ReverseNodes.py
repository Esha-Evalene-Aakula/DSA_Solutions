class Solution:
    def reverseKGroup(self, head, k):
        if k <= 1 or not head:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self._getKth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            prev = group_next
            cur = group_prev.next
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def _getKth(self, node, k):
        cur = node
        for _ in range(k):
            cur = cur.next
            if not cur:
                return None
        return cur
