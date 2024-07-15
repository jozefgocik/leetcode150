# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    # def jump(self, nums):
    #     result = 0
    #     currentIndex = 0
    #
    #     if len(nums) < 2:
    #         return 0
    #
    #     while currentIndex < len(nums):
    #         nextIndex = currentIndex
    #         nextIndexMaxValue = 0
    #         for i in range(0, nums[currentIndex] + 1):
    #             if currentIndex + i >= len(nums) - 1:
    #                 return result + 1
    #             elif nums[currentIndex + i] + i > nextIndexMaxValue:
    #                 nextIndex = currentIndex + i
    #                 nextIndexMaxValue = nums[currentIndex + i] + i
    #
    #         result += 1
    #         currentIndex = nextIndex
    #
    #     return result

    # Solution 2
    # O(n) time / O(1) space
    def jump(self, nums):
        result = 0
        left, right = 0, 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            result += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.jump(nums=[2, 3, 1, 1, 4]))
    print(solution.jump(nums=[2, 3, 0, 1, 4]))
    print(solution.jump(nums=[2]))
