# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # O(n) time / O(1) space
    def removeDuplicates(self, nums):
        left = 0
        right = 1

        if not nums:
            return 0

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                right += 1

        return left + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates(nums=[1, 1, 2]))
    print(solution.removeDuplicates(nums=[1, 2, 3]))
    print(solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
