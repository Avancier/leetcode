# coding=utf-8
"""
给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。

该数字按照大小进行排列，最大的数在列表的最前面。
"""
class Solution:
	"""
	:type digits: List[int]
	:rtype: List[int]
	"""
	def plusOne(self, digits):
		carry = 1
		for i in reversed(xrange(len(digits))):
			digits[i] += carry
			carry = digits[i] / 10
			digits[i] %= 10

		if carry:
			digits = [1] + digits

		return digits

	def plusOne2(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		digits = [str(x) for x in digits]
		num = int(''.join(digits)) + 1
		return [int(x) for x in str(num)]


if __name__ == '__main__':
	print Solution().plusOne([9,9,9,9])
	print Solution().plusOne2([9,9,9,9])
