# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # initialize strings to store and manipulate data
        str1 = ''
        str2 = ''
        current = l1
        while (current.next is not None):
            str1 = str(current.val) + str1
            current = current.next
        str1 = str(current.val) + str1
        current = l2
        while (current.next is not None):
            str2 = str(current.val) + str2
            current = current.next
        str2 = str(current.val) + str2
        answer = str(int(str1) + int(str2))
        myList = ListNode()
        current = myList
        index = len(answer) - 1
        for x in reversed(answer):
            current.val = int(x)
            if index is not 0:
                current.next = ListNode()
                current = current.next
            index-=1
        return myList



















