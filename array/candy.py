# coding=utf-8

# Time: O(n)
# Space: O(n)

"""
有 N 个小孩站成一列。每个小孩有一个评级。

按照以下要求，给小孩分糖果：

每个小孩至少得到一颗糖果。

评级越高的小孩可以得到更多的糖果。

需最少准备多少糖果？
"""

import operator

class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		candies = [1 for _ in xrange(len(ratings))]
		for i in xrange(1, len(ratings)):
			if ratings[i] > ratings[i - 1]:

				candies[i] = candies[i - 1] + 1


		for i in reversed(xrange(1, len(ratings))):
			if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
				candies[i - 1] = candies[i] + 1

		return reduce(operator.add, candies)

if __name__ == '__main__':
#	result = Solution().candy([1,2,3,2,3,5,2,5])
	result = Solution().candy([1,1,1]) 
	print result
