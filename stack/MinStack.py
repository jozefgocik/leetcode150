# https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150

# Solution 1
# O(1) time / O(n) space
# class MinStack(object):
#     def __init__(self):
#         self.stack = []
#         self.cache = {}
#         self.min = None
#
#     def push(self, val):
#         self.stack.append(val)
#         self.cache[len(self.stack) - 1] = self.min
#         self.min = val if self.min is None else min(self.min, val)
#
#     def pop(self):
#         self.stack.pop()
#         self.min = self.cache[len(self.stack)]
#         self.cache.pop(len(self.stack))
#
#     def top(self):
#         return self.stack[-1]
#
#     def getMin(self):
#         return self.min

# Solution 2
# O(1) time / O(n) space
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.cache = {}

    def push(self, val):
        self.cache[len(self.stack)] = val if not self.stack else min(self.cache[len(self.stack) - 1], val)
        self.stack.append(val)

    def pop(self):
        self.stack.pop()
        self.cache.pop(len(self.stack))

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.cache[len(self.stack) - 1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # return -3
    minStack.pop()
    print(minStack.top())  # return 0
    print(minStack.getMin())  # return -2
