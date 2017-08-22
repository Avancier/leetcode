# coding=utf-8
# Time: O(n)
# Space: O(1)
# 落单的数
"""
给出2*n + 1 个的数字，除其中一个数字之外
其他每个数字均出现两次，找到这个数字。
"""

# example-> [1,2,2,1,3,4,3]
# return 4

import operator


class Solution:
	"""
	:type nums: List[int]
	:rtype: int
	"""
	def singleNumber(self, A):
		return reduce(operator.xor, A)

if __name__ == '__main__':
	print Solution().singleNumber([1,2,2,1,3,4,3])

