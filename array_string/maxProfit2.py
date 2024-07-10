# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def maxProfit(self, prices):
        maxProfit = 0

        for i in range(1, len(prices)):
            currentProfit = prices[i] - prices[i - 1]
            if currentProfit > 0:
                maxProfit += currentProfit

        return maxProfit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(prices=[1, 2, 3]))
    print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit(prices=[1, 2, 3, 4, 5]))
    print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
