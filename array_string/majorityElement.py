# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # Solution 1
    # O(n * log(n)) time / O(1) space
    # def majorityElement(self, nums):
    #     majorityElement = (None, 0)
    #
    #     current = nums[0]
    #     currentCount = 0
    #     for num in sorted(nums):
    #         if num == current:
    #             currentCount += 1
    #         else:
    #             if currentCount > majorityElement[1]:
    #                 majorityElement = (current, currentCount)
    #             current = num
    #             currentCount = 1
    #
    #     if currentCount > majorityElement[1]:
    #         majorityElement = (current, currentCount)
    #
    #     return majorityElement[0]

    # Solution 2
    # O(n) time / O(n) space
    # def majorityElement(self, nums):
    #     counts = {}
    #
    #     majorityElement = (None, 0)
    #
    #     for num in nums:
    #         if num not in counts:
    #             counts[num] = 0
    #         counts[num] += 1
    #
    #         if counts[num] > majorityElement[1]:
    #             majorityElement = (num, counts[num])
    #
    #     return majorityElement[0]

    # Solution 3
    # O(n * log(n)) time / O(n) space
    # def majorityElement(self, nums):
    #     return sorted(nums)[int(len(nums)/2)]

    # Solution 4
    # O(n) time / O(1) space
    def majorityElement(self, nums):
        majorityElement = (None, 0)

        for num in nums:
            if majorityElement[1] == 0:
                majorityElement = (num, 1)
            elif num == majorityElement[0]:
                majorityElement = (majorityElement[0], majorityElement[1] + 1)
            else:
                majorityElement = (majorityElement[0], majorityElement[1] - 1)

        return majorityElement[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement(nums=[3, 2, 3]))
    print(solution.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
