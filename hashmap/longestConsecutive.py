# https://leetcode.com/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def longestConsecutive(self, nums):
    #     cache = set(nums)
    #
    #     result = 0
    #     while cache:
    #         num = cache.pop()
    #         currentLength = 1
    #         currentNum = num - 1
    #         while currentNum in cache:
    #             cache.remove(currentNum)
    #             currentNum -= 1
    #             currentLength += 1
    #
    #         currentNum = num + 1
    #         while currentNum in cache:
    #             cache.remove(currentNum)
    #             currentNum += 1
    #             currentLength += 1
    #
    #         result = max(result, currentLength)
    #
    #     return result

    # Solution 2
    # O(n) time / O(n) space
    def longestConsecutive(self, nums):
        cache = set(nums)

        result = 0
        for num in cache:
            if num - 1 not in cache:
                currentLength = 0
                while num + currentLength in cache:
                    currentLength += 1

                result = max(result, currentLength)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
