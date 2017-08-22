# coding=utf-8
# Time: O(n)
# Space: O(1)
'''
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油gas[i]，并且从第_i_个加油站前往第_i_+1个加油站需要消耗汽油cost[i]。

你有一辆油箱容量无限大的汽车，现在要从某一个加油站出发绕环路一周，一开始油箱为空。

求可环绕环路一周时出发的加油站的编号，若不存在环绕一周的方案，则返回-1。

'''

class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		start, total_sum, current_sum = 0, 0, 0
		for i in xrange(len(gas)):
			diff = gas[i] - cost[i]
			current_sum += diff
			total_sum += diff
			if current_sum < 0:
				start = i +1
				current_sum = 0
		if total_sum >=0:
			return start

		return -1

if __name__ == '__main__':
	print Solution().canCompleteCircuit([1, 2, 3], [3, 2, 1])
	print Solution().canCompleteCircuit([1, 2, 3], [2, 2, 2])
	print Solution().canCompleteCircuit([1, 2, 3], [1, 2, 3])
	print Solution().canCompleteCircuit([1, 2, 3], [1, 2, 4])
