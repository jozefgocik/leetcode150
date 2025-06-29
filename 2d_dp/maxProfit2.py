# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/?envType=study-plan-v2&envId=top-interview-150

class Solution:

    # Solution 1
    # O(n ^ 2) time / O(n ^ 2) space
    def maxProfit(self, k, prices):
        cache = {}

        def dfs(index, holding, transactions, buy_price):
            if index >= len(prices) or transactions == k:
                return 0

            key = (index, holding, transactions)
            if key in cache:
                return cache[key]

            result = dfs(index + 1, holding, transactions, buy_price)
            if not holding:
                result = max(result, -prices[index] + dfs(index + 1, True, transactions, prices[index]))
            else:
                result = max(result, prices[index] + dfs(index + 1, False, transactions + 1, 0))

            cache[key] = result
            return result

        return dfs(0, False, 0, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(k=2, prices=[2, 4, 1]))
    print(solution.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
