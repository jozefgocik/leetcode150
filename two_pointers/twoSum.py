# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                break

        return [left + 1, right + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
    print(solution.twoSum(numbers=[2, 3, 4], target=6))
    print(solution.twoSum(numbers=[-1, 0], target=-1))
