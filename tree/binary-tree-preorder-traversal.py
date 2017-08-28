# coding=utf-8
# 给出一棵二叉树，返回其节点值的后序遍历。

# Time: O(n)
# Space: O(1)

# Given binary tree {1,#,2,3},
# return [1,2,3]

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Morris Traversal Solution
class Solution(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		result, curr = [], root
		while curr:
			if curr.left is None:
				result.append(curr.val)
				curr = curr.right
			else:
				node = curr.left
				while node.right and node.right != curr:
					node = node.right

				if node.right is None:
					result.append(curr.val)
					node.right = curr
					curr = curr.left
				else:
					node.right = None
					curr = curr.right

		return result

# Time: O(n)
# Space: O(h)
# Stack Solution
class Solution2(object):
	def preordertraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		result, stack = [], [(root, False)]
		while stack:
			root, is_visited = stack.pop()
			if root is None:
				continue
			if is_visited:
				result.append(root.val)
			else:
				stack.append((root.right, False))
				stack.append((root.left, False))
				stack.append((root, True))
		return result

if __name__ == '__main__':
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)
	result = Solution().preorderTraversal(root)
	print result
