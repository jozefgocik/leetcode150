# https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def convert(self, s, numRows):
    #     cache = ["" for _ in range(numRows)]
    #
    #     index = 0
    #     isGoingUp = False
    #     for char in s:
    #         if index == numRows - 1:
    #             isGoingUp = True
    #         if index == 0:
    #             isGoingUp = False
    #
    #         if isGoingUp:
    #             cache[index % numRows] += char
    #             index -= 1
    #         else:
    #             cache[index % numRows] += char
    #             index += 1
    #
    #     return ''.join(cache)

    # Solution 2
    # O(n) time / O(n) space
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        result = ""
        for i in range(numRows):
            increment = (numRows - 1) * 2
            for j in range(i, len(s), increment):
                result += s[j]
                if i in range(1, numRows - 1) and j + increment - 2 * i < len(s):
                    result += s[j + increment - 2 * i]

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert(s="PAYPALISHIRING", numRows=3))
    print(solution.convert(s="PAYPALISHIRING", numRows=4))
    print(solution.convert(s="A", numRows=1))
    print(solution.convert(s="ABC", numRows=1))
