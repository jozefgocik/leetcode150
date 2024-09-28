# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def isValid(self, s):
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif stack:
                current = stack.pop()
                if brackets[current] != char:
                    return False
            else:
                return False

        return not stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid(s="()"))
    print(solution.isValid(s="()[]{}"))
    print(solution.isValid(s="(]"))
    print(solution.isValid(s="([])"))
