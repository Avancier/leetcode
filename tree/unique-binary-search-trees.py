# coding=utf-8
# Time: O(n)
# Space: O(1)

# 不同的二叉查找树

# 给出 n，问由 1...n 为节点组成的不同的二叉查找树有多少种？

# 给出n = 3，有5种不同形态的二叉查找树：

# Math solution.
class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 0:
			return 1

		def combination(n, k):
			count = 1
			# C(n,k) = (n) / 1 * (n - 1) / 2 ... * (n - k + 1) / k
			for i in xrange(1, k + 1):
				count = count * (n - i + 1) / i;
			return count

		return combination(2 * n, n) - combination(2 * n, n - 1)


# Time: O(n^2)
# Space: O(n)
# DP solution
class Solution2:
	# @return an integer
	def numTrees(self, n):
		counts = [1, 1]
		for i in xrange(2, n + 1):
			count = 0
			for j in xrange(i):
				count += counts[j] * counts[i - j - 1]
			counts.append(count)
		return counts[-1]
	
if __name__ == "__main__":
	print Solution().numTrees(3)
