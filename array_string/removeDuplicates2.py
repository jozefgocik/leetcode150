# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # O(n) time / O(1) space
    def removeDuplicates(self, nums):
        left = 0
        right = 1
        current = 1

        if not nums:
            return 0

        while right < len(nums):
            if nums[left] == nums[right]:
                if current < 2:
                    left += 1
                    if left < right:
                        self.swap(nums, left, right)
            else:
                left += 1
                if left < right:
                    self.swap(nums, left, right)

                current = 0

            right += 1
            current += 1

        return left + 1

    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
    print(solution.removeDuplicates(nums=[1, 2, 2, 3]))
    print(solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
