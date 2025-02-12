# https://leetcode.com/problems/single-number-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def singleNumber(self, nums):
        a, b = 0, 0
        for num in nums:
            b = b ^ (a & num)
            a = a ^ num
            not_three = ~(a & b)

            a, b = not_three & a, not_three & b

        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber(nums=[2, 2, 3, 2]))
    print(solution.singleNumber(nums=[0, 1, 0, 1, 0, 1, 99]))
