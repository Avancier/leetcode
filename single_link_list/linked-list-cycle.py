# coding=utf-8
# Time: O(n)
# Space: O(1)

# 带环链表
# 给定一个链表，判断它是否有环。

# Given -21->10->4->5, tail connets to node index1
# return true

# Definition for singlty-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# @param head, a ListNode
	# @return a boolean
	def hasCycle(self, head):
		fast, slow = head, head
		while fast and fast.next:
			fast, slow = fast.next.next, slow.next
			if fast is slow:
				return True
		return False


if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = head.next
	print Solution().hasCycle(head)

