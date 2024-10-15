# https://leetcode.com/problems/lru-cache/?envType=study-plan-v2&envId=top-interview-150

# Solution 1
# O(1) time / O(n) space
class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.previous = self.right, self.left

    def insert(self, node):
        previous = self.right.previous
        node.previous = previous
        previous.next = node
        node.next = self.right
        self.right.previous = node
        self.cache[node.key] = node

    def remove(self, node):
        previous = node.previous
        previous.next = node.next
        node.next.previous = previous
        self.cache.pop(node.key)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            self.remove(self.left.next)


class Node(object):

    def __init__(self, key, value, previous=None, next=None):
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
