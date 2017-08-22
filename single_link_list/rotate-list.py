# coding=utf-8
# Time: O(n)
# Space: O(1)

# 旋转链表
"""
给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数
"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, repr(self.next))

	
class Solution(object):
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head


		n, cur = 1, head
		while cur.next:
			cur = cur.next
			n += 1
		cur.next = head

		cur, tail = head, cur
		for _ in xrange(n - k % n):
			tail = cur
			cur = cur.next
		tail_next = None

		return cur

if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
	print Solution().rotateRight(head, 2)
