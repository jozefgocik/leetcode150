# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * k) time / O(1) space
    # def rotate(self, nums, k):
    #     k = k % len(nums)
    #     for i in range(k):
    #         current = None
    #         for j in range(len(nums)):
    #             if current is None:
    #                 current = nums[j]
    #
    #             index = (j + 1) % len(nums)
    #             temp = nums[index]
    #             nums[index] = current
    #             current = temp
    #
    #     return nums

    # Solution 2
    # O(n) time / O(n) space
    # def rotate(self, nums, k):
    #     result = [None for _ in range(len(nums))]
    #
    #     for i in range(len(nums)):
    #         index = (i + k) % len(nums)
    #         result[index] = nums[i]
    #
    #     for j in range(len(result)):
    #         nums[j] = result[j]
    #
    #     return nums

    # Solution 3
    # O(n) time / O(1) space
    def rotate(self, nums, k):
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

        return nums

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
    print(solution.rotate(nums=[-1, -100, 3, 99], k=2))
    print(solution.rotate(nums=[-1], k=2))
