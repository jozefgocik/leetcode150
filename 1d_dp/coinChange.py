# https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) / O(n) space; n = amount, m = len(coins)
    # def coinChange(self, coins, amount):
    #     cache = {}
    #
    #     def dfs(coins, current):
    #         nonlocal cache
    #         if current in cache:
    #             return cache[current]
    #         if current < 0:
    #             return float("inf")
    #         if current == 0:
    #             return 0
    #
    #         result = float("inf")
    #         for coin in coins:
    #             res = dfs(coins, current - coin)
    #             if res != float("inf"):
    #                 result = min(result, res + 1)
    #
    #         cache[current] = result
    #         return result
    #
    #     res = dfs(coins, amount)
    #     return res if res != float("inf") else -1

    # Solution 2
    # O(n * m) / O(n) space; n = amount, m = len(coins)
    def coinChange(self, coins, amount):
        cache = [float("inf") for _ in range(amount + 1)]
        cache[0] = 0

        for value in range(1, amount + 1):
            for coin in coins:
                current = value - coin
                if current >= 0:
                    cache[value] = min(cache[value], cache[current] + 1)

        return cache[amount] if cache[amount] != float("inf") else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange(coins=[1, 2, 5], amount=11))
    print(solution.coinChange(coins=[2], amount=3))
    print(solution.coinChange(coins=[1], amount=0))
