# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(log(n)) time / O(1) space
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        index = self.searchRangeHelper(nums, target, 0, len(nums) - 1)
        if index == -1:
            return [-1, -1]

        left, right = index, index
        while left > 0 and nums[left - 1] == target:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] == target:
            right += 1

        return [left, right]

    def searchRangeHelper(self, nums, target, left, right):
        if left == right:
            return left if nums[left] == target else -1

        index = (left + right) // 2
        if nums[index] > target:
            return self.searchRangeHelper(nums, target, left, index)
        elif nums[index] < target:
            return self.searchRangeHelper(nums, target, index + 1, right)
        else:
            return index


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
    print(solution.searchRange(nums=[], target=0))
