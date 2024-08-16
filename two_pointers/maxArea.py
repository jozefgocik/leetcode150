# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        result = float("-inf")

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            result = max(result, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solution.maxArea(height=[1, 1]))
