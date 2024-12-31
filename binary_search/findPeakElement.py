# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # Avg: O(log(n)) time / O(1) space
    # Worst: O(n) time / O(1) space
    # def findPeakElement(self, nums):
    #     return self.findPeakElementHelper(nums, 0, len(nums) - 1)
    #
    # def findPeakElementHelper(self, nums, left, right):
    #     if left == right:
    #         return left if self.isPeak(nums, left) else None
    #
    #     index = (left + right) // 2
    #     if self.isPeak(nums, index):
    #         return index
    #
    #     leftSubtree = self.findPeakElementHelper(nums, left, index)
    #     rightSubtree = self.findPeakElementHelper(nums, index + 1, right)
    #
    #     return leftSubtree if leftSubtree is not None else rightSubtree
    #
    # def isPeak(self, nums, index):
    #     if len(nums) == 1:
    #         return True
    #     elif index == 0:
    #         return nums[index] > nums[index + 1]
    #     elif index == len(nums) - 1:
    #         return nums[index] > nums[index - 1]
    #
    #     return nums[index] > nums[index - 1] and nums[index] > nums[index + 1]

    # Solution 2
    # O(log(n)) time / O(1) space
    # def findPeakElement(self, nums):
    #     return self.findPeakElementHelper(nums, 0, len(nums) - 1)
    #
    # def findPeakElementHelper(self, nums, left, right):
    #     if left == right:
    #         return left if self.isPeak(nums, left) else None
    #
    #     index = (left + right) // 2
    #     if self.isPeak(nums, index):
    #         return index
    #
    #     leftNeighbor = float("-inf") if index == 0 else nums[index - 1]
    #     rightNeighbor = float("-inf") if index == len(nums) - 1 else nums[index + 1]
    #
    #     if leftNeighbor > rightNeighbor:
    #         return self.findPeakElementHelper(nums, left, index)
    #     else:
    #         return self.findPeakElementHelper(nums, index + 1, right)
    #
    # def isPeak(self, nums, index):
    #     if len(nums) == 1:
    #         return True
    #     elif index == 0:
    #         return nums[index] > nums[index + 1]
    #     elif index == len(nums) - 1:
    #         return nums[index] > nums[index - 1]
    #
    #     return nums[index] > nums[index - 1] and nums[index] > nums[index + 1]

    # Solution 3
    # O(log(n)) time / O(1) space
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            index = left + ((right - left) // 2)

            if index > 0 and nums[index] < nums[index - 1]:
                right = index - 1
            elif index < len(nums) - 1 and nums[index] < nums[index + 1]:
                left = index + 1
            else:
                return index


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPeakElement(nums=[1, 2, 3, 1]))
    print(solution.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]))
