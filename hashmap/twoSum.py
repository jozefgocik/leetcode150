# https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(1) space
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # Solution 2
    # O(n) time / O(n) space
    def twoSum(self, nums, target):
        cache = {}
        for i, num in enumerate(nums):
            otherNum = target - num
            if otherNum in cache:
                return [cache[otherNum], i]

            cache[num] = i


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
    print(solution.twoSum(nums=[3, 2, 4], target=6))
    print(solution.twoSum(nums=[3, 3], target=6))
