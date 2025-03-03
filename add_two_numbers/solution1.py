from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.current = head

    def __next__(self):
        if self.current:
            self.current = self.current.next
            return self.current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

    def format(self):
        ls = []
        ls.append(self.head.val)
        for node in iter(self):
            if node:
                ls.append(node.val)
        return ls[::-1]


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ll1 = LinkedList(l1)
        ll2 = LinkedList(l2)

        l1 = ll1.format()
        l2 = ll2.format()

        res = str(int("".join(map(str, l1))) + int("".join(map(str, l2))))
        prev = ListNode(val=int(res[0]), next=None)
        now = None
        for val in res[1:]:
            now = ListNode(val=int(val), next=prev)
            prev = now
        if len(res) == 1:
            return prev
        return now
