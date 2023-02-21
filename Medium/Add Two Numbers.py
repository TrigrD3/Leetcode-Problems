from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
    


# This code defines a class called "Solution" that contains a method called "addTwoNumbers" that takes in two singly-linked lists represented as ListNode objects, l1 and l2. The method returns a new singly-linked list that represents the sum of the two input lists.

# Each ListNode object has two attributes: val, which represents the value of the node, and next, which points to the next node in the linked list.

# The method initializes a dummy node called dummyHead and a pointer called curr that initially points to the dummyHead. It also initializes a carry variable to 0.

# The method then enters a while loop that iterates until both l1 and l2 are None and carry is 0. Within each iteration of the loop, the method calculates the sum of the current column by adding the values of the corresponding nodes in l1 and l2, as well as any carry from the previous column. The carry for the next column is calculated by integer division by 10. A new node is created with the units digit of the sum, and this node is added to the end of the result linked list. The curr pointer is then updated to point to the new node.

# After each iteration, l1 and l2 are updated to point to the next node in their respective linked lists, or None if there are no more nodes.

# Finally, the method returns the next node after the dummyHead node, which represents the head of the result linked list.