# https://leetcode.com/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(n) space
    # def lengthOfLIS(self, nums):
    #     cache = {}
    #
    #     def dfs(index):
    #         nonlocal cache
    #         if index in cache:
    #             return cache[index]
    #         if index == len(nums) - 1:
    #             return 1
    #
    #         result = 1
    #         for j in range(index + 1, len(nums)):
    #             if nums[index] < nums[j]:
    #                 res = dfs(j) + 1
    #                 result = max(result, res)
    #
    #         cache[index] = result
    #         return result
    #
    #     longest = float("-inf")
    #     for i in range(0, len(nums)):
    #         longest = max(longest, dfs(i))
    #
    #     return longest

    # Solution 1
    # O(n ^ 2) time / O(n) space
    def lengthOfLIS(self, nums):
        result = 1
        cache = [1 for _ in range(len(nums))]

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], cache[j] + 1)

            result = max(result, cache[i])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
    print(solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
    print(solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
