# coding=utf-8

# Time: O(n)
# Space: O(1)

"""
给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。

我们可以使用整数 0，1 和 2 分别代表红，白，蓝。
颜色分类
"""

class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		def triPartition(nums, target):
			i, j, n = 0, 0, len(nums) - 1

			while j <= n:
				if nums[j] < target:
					nums[i], nums[j] = nums[j], nums[i]
					i += 1
					j += 1
				elif  nums[j] > target:
					nums[j], nums[n] = nums[n], nums[j]
					n -= 1
				else:
					j += 1

		triPartition(nums, 1)

if __name__ == '__main__':
	A = [2, 1, 1, 0, 0, 2]
	Solution().sortColors(A)
	print A
