# https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 3) time / O(1) space
    # def threeSum(self, nums):
    #     result = []
    #
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             for k in range(j + 1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in result:
    #                     result.append(sorted([nums[i], nums[j], nums[k]]))
    #
    #     return result

    # Solution 2
    # O(n ^ 2) time / O(n) space
    def threeSum(self, nums):
        result = []

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    result.append(sorted([nums[i], nums[left], nums[right]]))
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum(nums=[0, 1, 1]))
    print(solution.threeSum(nums=[0, 0, 0]))
    print(solution.threeSum(nums=[-1, 0, 1, 0]))
    print(solution.threeSum(nums=[-2, 0, 0, 2, 2]))
    print(solution.threeSum(nums=[-2, 1, 4]))
