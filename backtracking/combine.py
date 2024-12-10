# https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ k) / O(n ^ k) space
    # def combine(self, n, k):
    #     array = [i + 1 for i in range(n)]
    #     result = []
    #
    #     def dfs(index, current):
    #         if len(current) == k:
    #             result.append(current)
    #             return
    #         if index >= n:
    #             return
    #
    #         for i in range(index, n):
    #             dfs(i + 1, current + [array[i]])
    #
    #     dfs(0, [])
    #     return result

    # Solution 2
    # O(n ^ k) / O(n ^ k) space
    def combine(self, n, k):
        result = []

        def dfs(index, current):
            if len(current) == k:
                result.append(current.copy())
                return

            for i in range(index, n):
                current.append(i + 1)
                dfs(i + 1, current)
                current.pop()

        dfs(0, [])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(n=4, k=2))
    print(solution.combine(n=1, k=1))
