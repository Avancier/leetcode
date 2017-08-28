# coding=utf-8
# 合并两个排序链表
# Time: O(n)
# Space: O(1)

# 将两个排序链表合并为一个新的排序链表

# Given 1->3->8->11->15->null, 2->null
# return 1->2->3->8->11->15->null

# Definition for singly-linked list
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, self.next)

	
class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		curr = dummy = ListNode(0)
		while l1 and l2:
			if l1.val < l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
			curr = curr.next
		curr.next = l1 or l2
		return dummy.next


if __name__ == "__main__":
	l1 = ListNode(1)
	l1.next = ListNode(3)
	l1.next.next = ListNode(8)
	l1.next.next.next = ListNode(11)
	l1.next.next.next.next = ListNode(15)
	l2 = ListNode(2)
#	l2.next = ListNode(2)
	print Solution().mergeTwoLists(l1, l2)
	
