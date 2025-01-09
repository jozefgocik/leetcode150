# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(log(n)) time / O(1) space
    def findMin(self, nums):
        return self.findMinHelper(nums, 0, len(nums) - 1)

    def findMinHelper(self, nums, left, right):
        index = (left + right) // 2
        if nums[left] <= nums[right]:
            return nums[left]
        elif nums[left] <= nums[index]:
            return self.findMinHelper(nums, index + 1, right)
        else:
            return self.findMinHelper(nums, left, index)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin(nums=[3, 4, 5, 1, 2]))
    print(solution.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
    print(solution.findMin(nums=[11, 13, 15, 17]))
