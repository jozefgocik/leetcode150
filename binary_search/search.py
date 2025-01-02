# https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(log(n)) time / O(1) space
    def search(self, nums, target):
        return self.searchHelper(nums, target, 0, len(nums) - 1)

    def searchHelper(self, nums, target, left, right):
        if left == right:
            return left if nums[left] == target else -1

        index = (left + right) // 2
        if nums[index] == target:
            return index

        if nums[index] >= nums[left]:
            if target > nums[index] or nums[left] > target:
                return self.searchHelper(nums, target, index + 1, right)
            else:
                return self.searchHelper(nums, target, left, index)
        else:
            if target < nums[index] or target > nums[right]:
                return self.searchHelper(nums, target, left, index)
            else:
                return self.searchHelper(nums, target, index + 1, right)


if __name__ == '__main__':
    solution = Solution()
    print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(solution.search(nums=[1], target=0))
