# https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def romanToInt(self, s):
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        previousValue = float("-inf")
        for i in reversed(range(len(s))):
            currentValue = symbols[s[i]]
            if currentValue < previousValue:
                currentValue = -currentValue

            result += currentValue
            previousValue = symbols[s[i]]

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt(s="III"))
    print(solution.romanToInt(s="LVIII"))
    print(solution.romanToInt(s="MCMXCIV"))
