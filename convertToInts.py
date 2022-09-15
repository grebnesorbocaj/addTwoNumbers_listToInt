# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linkedToList(l1: Optional[ListNode]) -> Optional[int]:
            res = []
            while l1:
                res.append(l1.val)
                l1 = l1.next
            return res
        
        l1 = linkedToList(l1)
        l2 = linkedToList(l2)
        
        
        def listToInt(l1: Optional[int]) -> int:
            for i in range(len(l1)):
                l1[i] = str(l1[i])
            intStr = "".join(l1)
            return int(intStr)
        
        l1 = listToInt(l1)
        l2 = listToInt(l2)
        tot = int(l1) + int(l2)
        
        
        def intToList(val: int) -> Optional[int]:
            lst = list(str(val))
            for i in range(len(lst)):
                lst[i] = int(lst[i])
            return lst
        
        tot = intToList(tot)
        
        def listToLinked(lst: Optional[int]) -> Optional[ListNode]:
            head = curr = ListNode()
            for n in lst:
                curr.next = ListNode(n)
                curr = curr.next
            return head.next
        
        return listToLinked(tot)
        