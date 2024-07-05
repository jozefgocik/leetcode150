# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # O(n) time / O(1) space
    def removeElement(self, nums, val):
        k = len(nums)

        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[right] == val:
                right -= 1
                k -= 1
            elif nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                k -= 1
            else:
                left += 1

        return k


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement(nums=[3, 2, 2, 3], val=3))
    print(solution.removeElement(nums=[1], val=1))
