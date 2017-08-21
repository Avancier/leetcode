class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		dictMap = {}
		for index, value in enumerate(num):
			if target - value in dictMap:
				return dictMap[target - value] + 1, index + 1
			dictMap[value] = index

# debug
s = Solution()
print s.twoSum([2,7,11,15], 9)
