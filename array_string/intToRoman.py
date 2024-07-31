# https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def intToRoman(self, num):
        symbols = {1: "I", 4: "IV", 5: "V", 9: "IX",
                   10: "X", 40: "XL", 50: "L", 90: "XC",
                   100: "C", 400: "CD", 500: "D", 900: "CM",
                   1000: "M"}

        result = ""
        number = num
        while number > 0:
            for key in reversed(sorted(symbols)):
                while number >= key:
                    result += symbols[key]
                    number -= key

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(num=3749))
    print(solution.intToRoman(num=58))
    print(solution.intToRoman(num=1994))
