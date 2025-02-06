# https://leetcode.com/problems/add-binary/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(max(n, m)) time / O(max(n, m)) space
    def addBinary(self, a, b):
        i = 1
        carry = 0
        result = ""
        while i < max(len(a), len(b)) + 1:
            num1 = 0 if len(a) - i < 0 else int(a[len(a) - i])
            num2 = 0 if len(b) - i < 0 else int(b[len(b) - i])
            nums = num1 + num2 + carry
            result += "0" if nums % 2 == 0 else "1"
            carry = 0 if nums < 2 else 1
            i += 1

        if carry == 1:
            result += "1"

        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary(a="11", b="1"))
    print(solution.addBinary(a="11", b="0"))
    print(solution.addBinary(a="1010", b="1011"))
