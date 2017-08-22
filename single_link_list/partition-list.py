# coding=utf-8

# 链表划分

'''
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。

你应该保留两部分内链表节点原有的相对顺序。
'''

# example 
# given 1->4->3->2->5->2->null, x=3
# return 1->2->2->4->3->5->null

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, repr(self.next))


class Solution:
	# @param head, a ListNode
	# @param x, an integer
	# @return a ListNode
	def partition(self, head, x):
		dummySmaller, dummyGreater = ListNode(-1), ListNode(-1)
		smaller, greater = dummySmaller, dummyGreater

		while head:
			if head.val < x:
				smaller.next = head
				smaller = smaller.next
			else:
				greater.next = head
				greater = greater.next
			head = head.next

		smaller.next = dummyGreater.next
		greater.next = None

		return dummySmaller.next

if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(4)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(2)
	head.next.next.next.next = ListNode(5)
	head.next.next.next.next.next = ListNode(2)
	print Solution().partition(head, 3)
	
