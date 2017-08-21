# coding=utf-8
# 删除排序数组的重复数字
# Given input array A = [1,1,2]

# should return length =2, and A is now [1,2].

class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		if not A:
			return 0

		last, i = 0, 1
		while i < len(A):
			if A[last] != A[i]:
				last += 1
				A[last] = A[i]
			i += 1

		return last + 1


if __name__ == '__main__':
	print Solution().removeDuplicates([1,1,2])
