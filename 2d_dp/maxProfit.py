# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(n ^ 2) space
    # def maxProfit(self, prices):
    #     cache = {}
    #
    #     def dfs(index, holding, transactions, buy_price):
    #         if index >= len(prices) or transactions == 2:
    #             return 0
    #
    #         key = (index, holding, transactions, buy_price)
    #         if key in cache:
    #             return cache[key]
    #
    #         skip = dfs(index + 1, holding, transactions, buy_price)
    #         if not holding:
    #             buy = dfs(index + 1, True, transactions, prices[index])
    #             result = max(buy, skip)
    #         else:
    #             sell = prices[index] - buy_price + dfs(index + 1, False, transactions + 1, 0)
    #             result = max(sell, skip)
    #
    #         cache[key] = result
    #         return result
    #
    #     return dfs(0, False, 0, 0)

    # Solution 2
    # O(n) time / O(1) space
    def maxProfit(self, prices):
        buy1, buy2 = -prices[0], -prices[0]
        profit1, profit2 = 0, 0

        for price in prices:
            buy1 = max(buy1, -price)
            profit1 = max(profit1, price + buy1)
            buy2 = max(buy2, profit1 - price)
            profit2 = max(profit2, price + buy2)

        return profit2


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
    print(solution.maxProfit(prices=[1, 2, 3, 4, 5]))
    print(solution.maxProfit(prices=[7, 6, 4, 3, 1]))
    print(solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit(prices=[3, 2, 6, 5, 0, 3]))
