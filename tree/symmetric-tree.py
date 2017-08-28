# coding-utf8
# Time: O(n)
# Space: O(h)
# 对称树--判断一个二叉树是否是轴对称的
# Given a binary tree, check whether it is a mirror of itself 

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Iterative solution
class Solution:
	# @param root, a tree node
	# @return a boolean
	def isSymmetric(self, root):
		if root is None:
			return True
		stack = []
		stack.append(root.left)
		stack.append(root.right)

		while stack:
			p, q = stack.pop(), stack.pop()

			if p is None and q is None:
				continue

			if p is None or q is None or p.val != q.val:
				return False

			stack.append(p.left)
			stack.append(q.right)

			stack.append(p.right)
			stack.append(q.right)

		return True

# Recursive solution
class Solution2:
	# @param root, a tree node
	# @return a boolean
	def isSymmetric(self, root):
		if root is None:
			return True

		return self.isSymmetricRecu(root.left, root.right)

	def isSymmetricRecu(self, left, right):
		if left is None and right is None:
			return True
		if left is None or right is None or left.val != right.val:
			return False
		return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)


if __name__ == "__main__":
	root = TreeNode(1)
	root.left, root.right = TreeNode(2), TreeNode(2)
	root.left.left, root.right.right = TreeNode(3), TreeNode(3)
	root.left.right, root.right.left = TreeNode(4), TreeNode(4)
	print Solution().isSymmetric(root)
