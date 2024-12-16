# https://leetcode.com/problems/generate-parentheses/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(2^n) time / O(n) space
    def generateParenthesis(self, n):
        result = []

        def dfs(left, right, current):
            if left == 0 and right == 0:
                result.append(current)
                return

            if left > 0:
                dfs(left - 1, right, current + "(")
            if right > left:
                dfs(left, right - 1, current + ")")

        dfs(n, n, "")

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(n=3))
    print(solution.generateParenthesis(n=1))
