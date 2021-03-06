# coding=utf-8
# Time: O(n)
# Space: O(n)
# 前序遍历和中序遍历树构造二叉树

"""
给定一个二叉树的先序遍历和中序遍历，构造出一颗二叉树。

二叉树的遍历分为先序遍历、中序遍历、后序遍历、层序遍历。

而通过先序遍历和中序遍历、中序遍历和后序遍历 是可以还原该二叉树结构的。
"""
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	
class Solution:
	# @param preorder, a list of integers
	# @param inorder, a list of integers
	# @return a tree node
	def buildTree(self, preorder, inorder):
		lookup = {}
		for i, num in enumerate(inorder):
			lookup[num] = i
		return self.buildTreeRecu(lookup, preorder, inorder, 0, 0, len(inorder))

	def buildTreeRecu(self, lookup, preorder, inorder, pre_start, in_start, in_end):
		if in_start == in_end:
			return None
		node = TreeNode(preorder[pre_start])
		i = lookup[preorder[pre_start]]
		node.left = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1, in_start, i)
		node.right = self.buildTreeRecu(lookup, preorder, inorder, pre_start +1 + i - in_start, i + 1, in_end)
		return node

if __name__ == "__main__":
	preorder = [1,2,3]
	inorder = [2,1,3]
	result = Solution().buildTree(preorder, inorder)
	print result.val
	print result.left.val
	print result.right.val

