# coding=utf-8
# 二叉树的层次遍历

# 给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）

# Time: O(n)
# Space: O(n)

# ex
# Given binary tree {3,9,20,#,#,15,7},

# return its level order traversal as:
# [ [3], [9, 20], [15, 7] ]

# Definition for a binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right =None

	
class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrder(self, root):
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
		return result

if __name__ == '__main__':
	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)
	result = Solution().levelOrder(root)
	print result

