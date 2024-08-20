# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def minSubArrayLen(self, target, nums):
        left = 0
        currentSum = 0
        result = float("inf")

        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum >= target:
                result = min(result, right - left + 1)
                currentSum -= nums[left]
                left += 1

        return 0 if result == float("inf") else result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
    print(solution.minSubArrayLen(target=4, nums=[1, 4, 4]))
    print(solution.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
