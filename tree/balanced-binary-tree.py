# coding=utf-8
# Time: O(n)
# Space: O(h)

"""
给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的
二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。 

given binary tree A= {3,9,20,#,#,15,7}, B={3,#,20,15,7}

"""
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		return (self.getHeight(root) >= 0)

	def getHeight(self, root):
		if root is None:
			return 0
		left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
		if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
			return -1
		return max(left_height, right_height) + 1


if __name__ == '__main__':
	root = TreeNode(0)
	root.left = TreeNode(1)
	result = Solution().isBalanced(root)
	print result

	root.left.left = TreeNode(2)
	result = Solution().isBalanced(root)
	print result
