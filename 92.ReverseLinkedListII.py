# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        """
        begin
        temp
        pm
        pn
        """
        
        if m == n:
            return head
        
        temp = head
        index = 1
        pre = None
        
        while index!=n+1:
            if index == m-1:
                next_item = temp.next
                begin = temp
            elif index == m:
                pm = temp
                next_item = temp.next
                pre = temp
            elif index < n and index >m:
                next_item = temp.next
                temp.next = pre
                pre =temp
            elif index == n:
                pn = temp
                pm.next = temp.next
                temp.next = pre
                if m != 1:
                    begin.next = temp
            else:
                next_item = temp.next
            index = index + 1
            temp = next_item
        if m>1:
            return head
        else:
            return pn