# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # Solution 1
    # O(n) time / O(1) space
    def maxProfit(self, prices):
        left = 0
        right = 0
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return maxProfit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
