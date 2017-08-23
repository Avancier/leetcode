# coding=utf-8

# Time: O(n)
# Space: O(1)

# 带环链表ii

"""
给定一个链表，如果链表中存在环，则返回到链表中环的
起始节点的值，如果没有环，返回null。
Given -21->10->4->5, taill connects to node index 1 
return 10
"""

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __str__(self):
		if self:
			return "{}".format(self.val)
		else:
			return None

class Solution:
	# @param head, a ListNode
	# @return a list node
	def detectCycle(self, head):
		fast, slow = head, head
		while fast and fast.next:
			fast, slow = fast.next.next, slow.next
			if fast is slow:
				fast = head
				while fast is not slow:
					fst, slow = fast.next, slow.next
				return fast
			return None

if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = head.next
	print Solution().detectCycle(head)

