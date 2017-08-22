# coding=utf-8
# Input: (2 -> 4 -> 3) + (5 -> 6 ->4)
# Output: 7 -> 0 -> 8
# 链表求和
'''
你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照
在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数
将两个整数相加，用链表形式返回和。
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	
class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		dummy = ListNode(0)
		current, carry = dummy, 0

		while l1 or l2:
			val = carry
			if l1:
				val += l1.val
				l1 = l1.next
			if l2:
				val += l2.val
				l2 = l2.next
			carry, val = val / 10, val % 10
			current.next = ListNode(val)
			current = current.next

		if carry == 1:
			current.next = ListNode(1)

		return dummy.next

if __name__ == '__main__':
	a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
	b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
	result = Solution().addTwoNumbers(a, b)
	print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)
