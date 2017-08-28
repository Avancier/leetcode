# coding=utf-8

# Time: O(n)
# Space: O(1)

# 丢失的第一个正整数
# 给出一个无序的正数数组，找出其中没有出现的最小正整数。

# Given [1,2,0] return 3
# and [3,4,-1,1] return 2


class Solution:
	# @param A, a list of integers
	# @return an integer
	def firstMissingPositive(self, A):
		i = 0
		while i < len(A):
			if A[i] > 0 and A[i] - 1 < len(A) and A[i] != A[A[i]-1]:
				A[A[i]-1], A[i] = A[i], A[A[i]-1]

			else:
				i += 1

		for i, integer in enumerate(A):
			if integer != i + 1:
				return i + 1
		return len(A) + 1

if __name__ == '__main__':
	print Solution().firstMissingPositive([1,2,0])
	print Solution().firstMissingPositive([3,4,-1,1])

