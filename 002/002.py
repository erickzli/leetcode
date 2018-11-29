# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        ret = ListNode(0)
        head = 1
        addition = 0
        
        while l1 != None and l2 != None:
            if head == 1:
                trav = ret
                head = 0
            else:
                trav.next = ListNode(0)
                trav = trav.next

            trav.val += (l1.val + l2.val + addition) % 10
            addition = (l1.val + l2.val + addition) // 10
            
            l1 = l1.next
            l2 = l2.next
            
        if l1 == None:
            while l2 != None:
                trav.next = ListNode(0)
                trav = trav.next
                trav.val += (l2.val + addition) % 10
                addition = (l2.val + addition) // 10
                
                l2 = l2.next
                
            
        if l2 == None:
            while l1 != None:
                trav.next = ListNode(0)
                trav = trav.next
                trav.val += (l1.val + addition) % 10
                addition = (l1.val + addition) // 10
                
                l1 = l1.next
                
            
        if addition != 0:
            trav.next = ListNode(addition)
            
        return ret
