# coding:utf-8

# Time: O(n)
# Space: O(1)

# 验证二叉查找树

"""
给定一个二叉树，判断它是否是合法的二叉查找树(BST)

一棵BST定义为：

节点的左子树中的值要严格小于该节点的值。
节点的右子树中的值要严格大于该节点的值。
左右子树也必须是二叉查找树。
一个节点的树也是二叉查找树。
"""

# Defination for a binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Morris Traversal Solution
class Solution:
	# @param root, a tree node
	# @return a list of integers
	def isValidBST(self, root):
		prev, cur = None, root
		while cur:
			if cur.left is None:
				if prev and prev.val >= cur.val:
					return False
				prev = cur
				cur = cur.right
			else:
				node = cur.right
				while node.right and node.right != cur:
					node = node.right

				if node.right is None:
					node.right = cur
					cur = cur.left
				else:
					if prev and prev.val >= cur.val:
						return False
					node.right = None
					prev = cur
					cur = cur.right

		return True

# Time: O(n)
# Space: O(h)
class Solution2:
	# @param root, a tree node
	# @return a boolean
	def isValidBST(self, root):
		return self.isValidBSTRecu(root, float("-inf"), float("inf"))

	def isValidBSTRecu(self, root, low, high):
		if root is None:
			return True

		return low < root.val and root.val < high \
			and self.isValidBSTRecu(root.left, low, root.val) \
			and self.isValidBSTRecu(root.right, root.val, high)

if __name__ == '__main__':
	root = TreeNode(2)
	root.left = TreeNode(1)
	root.right = TreeNode(3)
	print Solution().isValidBST(root)
