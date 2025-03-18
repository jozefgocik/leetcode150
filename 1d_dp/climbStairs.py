# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def climbStairs(self, n):
    #     cache = {}
    #
    #     def dfs(n, current):
    #         nonlocal cache
    #         if current in cache:
    #             return cache[current]
    #         if current == n:
    #             return 0
    #         if current > n:
    #             return -1
    #
    #         left = dfs(n, current + 1)
    #         right = dfs(n, current + 2) + 1
    #         total = left + right
    #         cache[current] = total
    #
    #         return total
    #
    #     return dfs(n, 0) + 1

    # Solution 2
    # O(n) time / O(n) space
    # def climbStairs(self, n):
    #     cache = [1, 1]
    #
    #     for _ in range(1, n):
    #         current, previous = cache[-1], cache[-2]
    #         cache.append(current + previous)
    #
    #     return cache[-1]

    # Solution 3
    # O(n) time / O(1) space
    def climbStairs(self, n):
        current, previous = 1, 1

        for _ in range(1, n):
            current, previous = current + previous, current

        return current


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(n=2))
    print(solution.climbStairs(n=3))
