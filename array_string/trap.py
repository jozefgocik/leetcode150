# https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # Solution 1
    # O(n) time / O(n) space
    # def trap(self, height):
    #     cache = [0 for _ in range(len(height))]
    #     currentMin = 0
    #     for i in range(len(height)):
    #         if height[i] < currentMin:
    #             cache[i] = currentMin - height[i]
    #         currentMin = max(currentMin, height[i])
    #
    #     currentMin = 0
    #     for i in reversed(range(len(height))):
    #         if height[i] < currentMin:
    #             cache[i] = min(cache[i], currentMin - height[i])
    #         else:
    #             cache[i] = 0
    #         currentMin = max(currentMin, height[i])
    #
    #     return sum(cache)

    # Solution 2
    # O(n) time / O(1) space
    def trap(self, height):
        if not height:
            return 0

        result = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                result += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                result += maxRight - height[right]

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solution.trap(height=[4, 2, 0, 3, 2, 5]))
