# coding=utf-8
# Time: O(n)
# Space: O(1)

# 重排链表
"""
给定一个单链表L: L0→L1→…→Ln-1→Ln,

重新排列后为：L0→Ln→L1→Ln-1→L2→Ln-2→…

必须在不改变节点值的情况下进行原地操作。

Given 1->2->3->4->null
1->4->2->3->null
"""

# Definition for singly-linked list
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, repr(self.next))

	
class Solution:
	# @param head, a ListNode
	# @return nothing
	def reorderList(self, head):
		if head == None or head.next == None:
			return head

		fast, slow, prev = head, head, None
		while fast != None and fast.next != None:
			fast, slow, prev = fast.next.next, slow.next, slow
		current, prev.next, prev = slow, None, None

		while current != None:
			current.next, prev, current = prev, current, current.next

		l1, l2 = head, prev
		dummy = ListNode(0)
		current = dummy

		while l1 != None and l2 != None:
			current.next, current, l1 = l1, l1, l1.next
			current.next, current, l2 = l2, l2, l2.next

		return dummy.next

if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	#head.next.next.next.next = ListNode(5)
	print Solution().reorderList(head)


