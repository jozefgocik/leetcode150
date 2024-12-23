# https://leetcode.com/problems/maximum-subarray/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def maxSubArray(self, nums):
        result = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0

            currentSum += num
            result = max(result, currentSum)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray(nums=[1]))
    print(solution.maxSubArray(nums=[5, 4, -1, 7, 8]))
