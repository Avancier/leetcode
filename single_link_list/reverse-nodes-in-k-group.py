# coding=utf-8
# Time: O(n)
# Space: O(1)
# K组翻转链表

"""
给你一个链表以及一个k,将这个链表从头指针开始每k个翻转一下。
链表元素个数不是k的倍数，最后剩余的不用翻转。
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

"""

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, repr(self.next))


class Solution:
	# @param head, a ListNode
	# @param k, an integer
	# @return a ListNode
	def reverseKGroup(self, head, k):
		dummy = ListNode(-1)
		dummy.next = head

		cur, cur_dummy = head, dummy
		length = 0

		while cur:
			next_cur = cur.next
			length = (length + 1) % k

			if length == 0:
				next_dummy = cur_dummy.next
				self.reverse(cur_dummy, cur.next)
				cur_dummy = next_dummy

			cur = next_cur

		return dummy.next

	def reverse(self, begin, end):
		first = begin.next
		cur = first.next

		while cur != end:
			first.next = cur.next
			cur.next = begin.next
			begin.next = cur
			cur = first.next

if __name__ == "__main__":
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
#	print Solution().reverseKGroup(head, 3)
	print Solution().reverseKGroup(head, 2)

