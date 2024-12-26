# https://leetcode.com/problems/maximum-sum-circular-subarray/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n^2) time / O(1) space
    # def maxSubarraySumCircular(self, nums):
    #     result = float("-inf")
    #     n = len(nums)
    #
    #     for i in range(n):
    #         currentSum = 0
    #         for j in range(i, i + n):
    #             currentSum = max(currentSum + nums[j % n], nums[j % n])
    #             result = max(result, currentSum)
    #
    #     return result

    # Solution 2
    # O(n) time / O(1) space
    def maxSubarraySumCircular(self, nums):
        globalMax, globalMin = float("-inf"), float("inf")
        currentMax, currentMin = 0, 0

        for i in range(len(nums)):
            currentMax = max(currentMax + nums[i], nums[i])
            currentMin = min(currentMin + nums[i], nums[i])
            globalMax = max(globalMax, currentMax)
            globalMin = min(globalMin, currentMin)

        if globalMax < 0:
            return globalMax

        return max(globalMax, sum(nums) - globalMin)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubarraySumCircular(nums=[1, -2, 3, -2]))
    print(solution.maxSubarraySumCircular(nums=[5, -3, 5]))
    print(solution.maxSubarraySumCircular(nums=[-3, -2, -3]))
