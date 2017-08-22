# coding=utf-8
# 格雷编码
"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个二进制的差异。

给定一个非负整数 n ，表示该代码中所有二进制的总数，请找出其格雷编码顺序。一个格雷编码顺序必须以 0 开始，并覆盖所有的 2n 个整数。
"""

# example , given n=2, return [0,1,3,2]. It's gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2

class Solution(object):
	def grayCode(self, n):
		"""
		:type n: int
		:rtypr: List[int]
		"""
		result = [0]
		for i in xrange(n):
			for n in reversed(result):
				result.append(1 << i | n)
		return result


# Proof of closed from formula could be found here:
# http://math.stackexchange.com/questions/425894/proof-of-closed-form-formula

class Solution2(object):
	def grayCode(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		return [i >> 1 ^ i for i in xrange(1 << n)]


if __name__ == '__main__':
	print Solution().grayCode(0)
	print Solution().grayCode(2)

