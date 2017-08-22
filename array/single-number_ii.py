# coding=utf-8
# 落单的数ii

"""
给出3*n + 1 个的数字，除其中一个数字之外
其他每个数字均出现三次，找到这个数字。
"""

# example -> [1,1,2,3,3,3,2,2,4,1] return 4

import collections


class Solution(object):
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		one, two = 0, 0
		for x in A:
			one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
		return one


class Solution2(object):
	# @param A, a list of integer
	# @return an integer
	# ~取反
	def singleNumber(self, A):
		one, two, carry = 0, 0, 0
		for x in A:
			two |= one & x
			one ^= x
			carry = one & two
			one &= ~carry
			two &= ~carry
		return one

	
	class Solution3(object):
		def singleNumber(self, nums):
			"""
			:type nums: List[int]
			:rtype: int
			"""
			return (collections.Counter(list(set(nums)) * 3) - collections.Counter(nums)). keys()[0]

	
	class Solution4(object):
		def singleNumber(self, nums):
			"""
			:type nums: List[int]
			:rtype: int
			"""
			return (sum(set(nums)) * 3 - sum(nums)) / 2


	class SolutonEX(object):
		# @param A, a list of integer
		# @return an integer
		# [1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
		def singleNumber(self, A):
			one, two, three = 0, 0, 0
			for x in A:
				one, two, three = (~x & one) | (x & ~one & ~two & ~three), (~x & two) | (x & one), (~x & three) | (x & two)

			return two


if __name__ == '__main__':
	print Solution().singleNumber([1,1,2,3,3,3,2,2,4,1])
