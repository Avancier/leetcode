# coding=utf-8
# Time: O(n)
# Space: O(n)

# 二叉树的锯齿形层次遍历

"""
给出一棵二叉树，返回其节点值的锯齿形层次遍历
（先从左往右，下一层再从右往左，层与层之间交替进行） 

ex -> Given binary tree {3,9,20,#,#,15,7},

return its zigzag level order traversal as:
	[ [3], [20,9], [15,7] ]
"""
# Definition for a binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def zigzagLevelOrder(self, root):
		if root is None:
			return []
		result, current, level = [], [root], 1
		while current:
			next_level, vals = [], []
			for node in current:
				vals.append(node.val)
				if node.left:
					next_level.append(node.left)
				if node.right:
					next_level.append(node.right)
			if level % 2:
				result.append(vals)
			else:
				result.append(vals[::-1])
			level += 1
			current = next_level
		return result

if __name__ == "__main__":
	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)
	result = Solution().zigzagLevelOrder(root)
	print result


