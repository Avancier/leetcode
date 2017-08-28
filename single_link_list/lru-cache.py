# coding=utf-8
# Time: O(1)
# Space: O(k)
# LRU缓存策略
"""
为最近最少使用（LRU）缓存策略设计一个数据结构，它应该支持以下操作：获取数据（get）和写入数据（set）。

获取数据get(key)：如果缓存中存在key，则获取其数据值（通常是正数），否则返回-1。

写入数据set(key, value)：如果key还没有在缓存中，则写入其数据值。当缓存达到上限，它应该在写入新数据之前删除最近最少使用的数据用来腾出空闲位置。
"""

class ListNode:
	def __init__(self, key, val):
		self.val = val
		self.val = key
		self.next = None
		self.prev = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, node):
		if self.head is None:
			self.head = node
		else:
			self.tail.next = node
			node.prev = self.tail
		self.tail = node

	def delete(self, node):
		if node.prev:
			node.prev.next = node.next
		else:
			self.head = node.prev
		if node.next:
			node.next.prev = node.prev
		else:
			self.tail = node.prev
		del node


class LRUCache:

	# @param capacity, an integer
	def __init__(self, capacity):
		self.list = LinkedList()
		self.dict = {}
		self.capacity = capacity
	
	def _insert(self, key, val):
		node = ListNode(key, val)
		self.list.insert(node)
		self.dict[key] = node

	# @return an integer
	def get(self, key):
		if key in self.dict:
			val = self.dict[key].val
			self.list.delete(self.dict[key])
			self._insert(key, val)
			return val
		return -1


	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, val):
		if key in self.dict:
			self.list.delete(self.dict[key])
		elif len(self.dict) == self.capacity:
			del self.dict[self.list.head.key]
			self.list.delete(self.list.head)
		self._insert(key, val)

import collections
class LRUCache2:
	def __init__(self, capacity):
		self.cache = collections.OrderedDict()
		self.capacity = capacity

	def get(self, key):
		if key not in self.cache:
			return -1
		val = self.cache[key]
		del self.cache[key]
		self.cache[key] = val
		return val
	
	def set(self, key, value):
		if key in self.cache:
			del self.cache[key]
		elif len(self.cache) == self.capacity:
			self.cache.popitem(last=Fasle)
		self.cache[key] = value

if __name__ == '__main__':
	cache = LRUCache(3)
	cache.set(1, 1)
	cache.set(2, 2)
	cache.set(3, 3)
	print cache.get(1)
	#cache.set(4, 4)
	print cache.get(2)

