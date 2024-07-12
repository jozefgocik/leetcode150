class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    # def canJump(self, nums):
    #     currentIndex = 0
    #
    #     while currentIndex < len(nums):
    #         if currentIndex + nums[currentIndex] >= len(nums) - 1:
    #             return True
    #
    #         i = 0
    #         nextIndex = currentIndex
    #         nextMaxValue = -1
    #         while i < nums[currentIndex]:
    #             if nextMaxValue <= (nums[currentIndex + i + 1] + i) and nums[currentIndex + i + 1] > 0:
    #                 nextIndex = currentIndex + i + 1
    #                 nextMaxValue = nums[currentIndex + i + 1] + i
    #             i += 1
    #
    #         if currentIndex == nextIndex:
    #             return False
    #
    #         currentIndex = nextIndex
    #
    #     return True

    # Solution 2
    # O(n) time / O(1) space
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump(nums=[2, 3, 1, 1, 4]))
    print(solution.canJump(nums=[3, 2, 1, 0, 4]))
    print(solution.canJump(nums=[3, 0, 8, 2, 0, 0, 1]))
