# coding=utf-8
# 删除链表中倒数第n个节点
# Time: O(n)
# Space: O(1)


# 给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数

# ex given list 1->2->3->4->5->null 和 n = 2
# delete back second node, is list: 1->2->3->5->null.

# Defintion for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


	def __repr__(self):
		if self is None:
			return "Nil"
		else:
			return "{} -> {}".format(self.val, repr(self.next))

class Solution:
	# @return a ListNode
	def removeNthFromEnd(self, head, n):
		dummy = ListNode(-1)
		dummy.next = head
		slow, fast = dummy, dummy

		for i in xrange(n):
			fast = fast.next

		while fast.next:
			slow, fast = slow.next, fast.next

		slow.next = slow.next.next


		return dummy.next

if __name__ == "__main__":
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)

	print Solution().removeNthFromEnd(head, 2)
