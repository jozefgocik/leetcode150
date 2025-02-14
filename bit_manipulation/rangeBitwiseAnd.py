# https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    # def rangeBitwiseAnd(self, left, right):
    #     result = left
    #     for num in range(left, right + 1):
    #         result = result & num
    #         if result == 0:
    #             return result
    #
    #     return result

    # Solution 2
    # O(1) time / O(1) space
    # def rangeBitwiseAnd(self, left, right):
    #     result = 0
    #
    #     for i in range(32):
    #         bit = (left >> i) & 1
    #         if not bit:
    #             continue
    #
    #         remainder = left % (1 << (i + 1))
    #         diff = (1 << (i + 1)) - remainder
    #         if right - left < diff:
    #             result = result | (1 << i)
    #
    #     return result

    # Solution 3
    # O(1) time / O(1) space
    def rangeBitwiseAnd(self, left, right):
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1

        return left << i


if __name__ == '__main__':
    solution = Solution()
    print(solution.rangeBitwiseAnd(left=5, right=7))
    print(solution.rangeBitwiseAnd(left=0, right=0))
    print(solution.rangeBitwiseAnd(left=1, right=2147483647))
