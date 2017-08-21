# coding=utf-8
# 删除排序数组中的重复数字ii
# O(n), O(1)
#
# Follow up for "Remove Duplicates":
# What if suplicates are allowed at most twice?
#
# For example,
# Given sorted array A = [1,1,1,2,2,3],
#
# Your function should return length = 5, and A is now [1,1,2,2,3].

'''
加一个变量记录一下元素出现的次数即可.
这题因为是已经排序的数组,所以一个变量即可解决.
如果是没有排序的数组,则需要引入一个hashmap来记录出现次数.
'''
class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		if not A:
			return 0

		last, i, same = 0, 1, False
		while i < len(A):
			if A[last] != A[i] or not same:
				same = A[last] == A[i]
				last += 1
				A[last] = A[i]
			i += 1

		return last + 1

if __name__ == '__main__':
	print Solution().removeDuplicates([1,1,1,2,2,3])

