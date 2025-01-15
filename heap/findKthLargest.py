# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * k) time / O(k) space
    # def findKthLargest(self, nums, k):
    #     kElements = [float("-inf") for _ in range(k)]
    #     for num in nums:
    #         for i in range(len(kElements)):
    #             if num > kElements[i]:
    #                 temp = kElements[i]
    #                 kElements[i] = num
    #                 for j in range(i + 1, len(kElements)):
    #                     temp, kElements[j] = kElements[j], temp
    #                 break
    #
    #     return kElements[-1]

    # Solution 2
    # O(n * log(n)) time / O(n) space
    def findKthLargest(self, nums, k):
        heap = MaxHeap(nums)
        for i in range(k - 1):
            heap.popMax()
        return heap.peek()


class MaxHeap(object):
    def __init__(self, array):
        self.array = array
        self.heapify(self.array)

    def heapify(self, array):
        for i in reversed(range(len(array))):
            self.siftDown(array, i)

    def siftDown(self, array, i):
        left = 2 * i + 1
        right = 2 * i + 2
        leftVal = float("-inf") if left >= len(array) else array[left]
        rightVal = float("-inf") if right >= len(array) else array[right]

        if leftVal == float("-inf") and rightVal == float("-inf"):
            return
        elif (leftVal > rightVal or leftVal == rightVal) and array[i] < leftVal:
            self.swap(array, i, left)
            self.siftDown(array, left)
        elif rightVal > leftVal and array[i] < rightVal:
            self.swap(array, i, right)
            self.siftDown(array, right)

    def popMax(self):
        self.swap(self.array, 0, len(self.array) - 1)
        self.array.pop()
        self.siftDown(self.array, 0)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

    def peek(self):
        return self.array[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
