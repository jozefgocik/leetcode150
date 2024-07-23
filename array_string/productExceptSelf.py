# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def productExceptSelf(self, nums):
    #     prefixes = []
    #     for i in range(len(nums)):
    #         currentNum = nums[i]
    #         if i == 0:
    #             prefixes.append(currentNum)
    #         else:
    #             prefixes.append(prefixes[i - 1] * currentNum)
    #
    #     postfixes = [0 for _ in range(len(nums))]
    #     for i in reversed(range(len(nums))):
    #         currentNum = nums[i]
    #         if i == len(nums) - 1:
    #             postfixes[i] = currentNum
    #         else:
    #             postfixes[i] = postfixes[i + 1] * currentNum
    #
    #     result = []
    #     for i in range(len(nums)):
    #         pre = 1 if i == 0 else prefixes[i - 1]
    #         post = 1 if i == len(nums) - 1 else postfixes[i + 1]
    #
    #         result.append(pre * post)
    #
    #     return result

    # Solution 2
    # O(n) time / O(1) space
    def productExceptSelf(self, nums):
        result = [None for _ in range(len(nums))]

        for i in range(len(nums)):
            prefix = 1 if i == 0 else nums[i - 1] * result[i - 1]
            result[i] = prefix

        postfix = 1
        for i in reversed(range(len(nums))):
            result[i] *= postfix
            postfix *= nums[i]

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf(nums=[1, 2, 3, 4]))
    print(solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
