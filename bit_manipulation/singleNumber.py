# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber(nums=[2, 2, 1]))
    print(solution.singleNumber(nums=[4, 1, 2, 1, 2]))
    print(solution.singleNumber(nums=[1]))
