# coding=utf-8
# Time: O(n)
# Space: O(n)

# 二叉树的层次遍历 II

"""
给出一棵二叉树，返回其节点值从底向上的层次序遍历（按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）


Given binary tree {3,9,20,#,#,15,7},

return its bottom-up level order traversal as:
	[	[15,7], [9, 20], [3] ] 
"""

# Definition for a binary tree node
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""

		if root is None:
			return []

		result, current = [], [root]
		while current:
			next_level, vals = [], []
			for node in current:
				vals.append(node.val)
				if node.left:
					next_level.append(node.left)
				if node.right:
					next_level.append(node.right)
			current = next_level
			result.append(vals)

		return result[::-1]

if __name__ == '__main__':
	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)
	result = Solution().levelOrderBottom(root)
	print result
