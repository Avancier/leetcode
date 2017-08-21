# coding: utf-8
# 一个数组中两个位置上的数和恰为target, 求这两个位置
'''
思路: 1、可以先排序再用双指针向中间夹逼,复杂度O(nlogn)
2、可以用Map记录出现的数,只要判断有没有和当前的数凑成target的数,
再找出来就行, 复杂度O(nlogn)而不是O(n), 因为Map也有复杂度
3、在2中的Map复杂度可以用数组来弥补,时间复杂度是O(n), 不过空间复杂度是O(MAXN)
'''

class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		# sort
		sorted_num = sorted(num)

		# two points
		left = 0
		right = len(num) - 1
		res = []
		while(left < right):
			sum = sorted_num[left] + sorted_num[right]
			if sum == target:
				# find out index
				break;
			elif sum > target:
				right -= 1
			else:
				left += 1

		if left == right:
			return -1, -1
		else:
			pos1 = num.index(sorted_num[left]) + 1
			pos2 = num.index(sorted_num[right]) + 1
			if pos1 == pos2:	#find again
				pos2 = num[pos1:].index(sorted_num[right]) + pos1 + 1

			return min(pos1, pos2), max(pos1, pos2)

# debug
s = Solution()
print s.twoSum([2, 7, 11, 15], 9)

