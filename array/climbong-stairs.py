# coding=utf-8
# 爬楼梯 
"""
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？
"""
class Solution:
	"""
	:type n : int
	:rtype: int
	"""
	def climbStairs(self, n):
		prev, current = 0, 1
		for i in xrange(n):
			prev, current = current, prev + current,
		return current

	# Time: O(2^n)
	# Space: O(n)
	def climbStairs1(self, n):
		if n == 1:
			return 1
		if n == 2:
			return 2
		return self.climbStairs(n - 1) + self.climbStairs(n - 2)

if __name__ == '__main__':
	result = Solution().climbStairs(2)
	print result
