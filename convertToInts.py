# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linkedToList(tmp_lst: Optional[ListNode]) -> Optional[int]:
            res = []
            while tmp_lst:
                res.append(tmp_lst.val)
                tmp_lst = tmp_lst.next
            return res
        
        l1_list = linkedToList(l1)
        l2_list = linkedToList(l2)
        
        
        def listToInt(tmp_lst: Optional[int]) -> int:
            for i in range(len(tmp_lst)):
                tmp_lst[i] = str(tmp_lst[i])
            intStr = "".join(tmp_lst)
            return int(intStr)
        
        l1_int = listToInt(l1_list)
        l2_int = listToInt(l2_list)
        tot = int(l1_int) + int(l2_int)
        
        
        def intToList(val: int) -> Optional[int]:
            lst = list(str(val))
            for i in range(len(lst)):
                lst[i] = int(lst[i])
            return lst
        
        tot_list = intToList(tot)
        
        def listToLinked(tmp_lst: Optional[int]) -> Optional[ListNode]:
            head = curr = ListNode()
            for n in tmp_lst:
                curr.next = ListNode(n)
                curr = curr.next
            return head.next
        
        return listToLinked(tot_list)
        