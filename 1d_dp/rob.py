# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def rob(self, nums):
        previous, current = 0, 0

        for num in nums:
            temp = max(num + previous, current)
            previous = current
            current = temp

        return current


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob(nums=[1, 2, 3, 1]))
    print(solution.rob(nums=[2, 7, 9, 3, 1]))
