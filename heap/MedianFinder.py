# https://leetcode.com/problems/find-median-from-data-stream/?envType=study-plan-v2&envId=top-interview-150
import heapq


class MedianFinder(object):

    # Solution 1
    # O(n * log(n)) time / O(n) space
    # def __init__(self):
    #     self.heap = []
    #
    # def addNum(self, num):
    #     self.heap.append(num)
    #
    # def findMedian(self):
    #     self.heap.sort()
    #     index = len(self.heap) // 2
    #     if len(self.heap) % 2 == 0:
    #         return float(self.heap[index - 1] + self.heap[index]) / 2
    #     return self.heap[index]

    # Solution 2
    # O(log(n)) time / O(n) space
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        heapq.heappush(self.maxHeap, num * -1)
        if (self.minHeap and self.maxHeap and (self.maxHeap[0] * -1) > self.minHeap[0]) or len(self.maxHeap) - len(self.minHeap) > 1:
            item = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, item * -1)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            item = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, item * -1)

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            num1, num2 = self.maxHeap[0] * -1, self.minHeap[0]
            return float(num1 + num2) / 2
        return self.maxHeap[0] * -1 if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
