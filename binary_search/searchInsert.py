# https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(log(n)) time / O(1) space
    # def searchInsert(self, nums, target):
    #     return self.searchInsertHelper(nums, target, 0, len(nums))
    #
    # def searchInsertHelper(self, nums, target, left, right):
    #     if right - left == 1:
    #         if target == nums[left] or target < nums[left]:
    #             return left
    #         return left + 1
    #
    #     index = ((right - left) // 2) + left
    #     if target < nums[index]:
    #         return self.searchInsertHelper(nums, target, left, index)
    #     else:
    #         return self.searchInsertHelper(nums, target, index, right)

    # Solution 2
    # O(log(n)) time / O(1) space
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            index = (left + right) // 2

            if nums[index] == target:
                return index

            if target <= nums[index]:
                right = index - 1
            else:
                left = index + 1

        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert(nums=[1, 3, 5, 6], target=5))
    print(solution.searchInsert(nums=[1, 3, 5, 6], target=2))
    print(solution.searchInsert(nums=[1, 3, 5, 6], target=7))
