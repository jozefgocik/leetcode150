# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def calculate(self, s):
    #     i = 0
    #     return self.calculateHelper(s, i)[0]
    #
    # def calculateHelper(self, s, i):
    #     current = 0
    #     sign = None
    #     while i < len(s):
    #         if s[i] == "(":
    #             temp, index = self.calculateHelper(s, i + 1)
    #             current = self.calculateNums(current, temp, sign)
    #             i = index
    #         elif s[i] == ")":
    #             return current, i
    #         elif s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
    #             sign = s[i]
    #         elif s[i].isnumeric():
    #             num = s[i]
    #             while i < len(s) - 1 and s[i + 1].isnumeric():
    #                 i += 1
    #                 num += s[i]
    #             current = self.calculateNums(current, int(num), sign)
    #         i += 1
    #
    #     return current, i
    #
    # def calculateNums(self, a, b, sign):
    #     if sign is None:
    #         a = b
    #     elif sign == "+":
    #         a += b
    #     elif sign == "-":
    #         a -= b
    #     elif sign == "*":
    #         a *= b
    #     elif sign == "/":
    #         a /= b
    #
    #     return a

    # Solution 2
    # O(n) time / O(n) space
    def calculate(self, s):
        result = 0
        current = 0
        sign = 1
        stack = []
        for char in s:
            if char.isdigit():
                current = current * 10 + int(char)
            elif char in "+-":
                result += current * sign
                current = 0
                if char == "+":
                    sign = 1
                else:
                    sign = -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += current * sign
                result *= stack.pop()
                result += stack.pop()
                current = 0

        return result + (current * sign)


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate(s="1 + 1"))
    print(solution.calculate(s=" 2-1 + 2 "))
    print(solution.calculate(s="(1+(4+5+2)-3)+(6+8)"))
