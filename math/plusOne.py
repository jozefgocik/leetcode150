# https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def plusOne(self, digits):
    #     temp = str(int("".join(str(i) for i in digits)) + 1)
    #     result = []
    #
    #     for char in temp:
    #         result.append(int(char))
    #
    #     return result

    # Solution 2
    # O(n) time / O(n) space
    def plusOne(self, digits):
        remainder = 1
        result = []

        for num in digits[::-1]:
            if remainder == 1:
                if num == 9:
                    num = 0
                else:
                    num += 1
                    remainder -= 1
            result.append(num)

        if remainder == 1:
            result.append(remainder)

        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne(digits=[1, 2, 3]))
    print(solution.plusOne(digits=[4, 3, 2, 1]))
    print(solution.plusOne(digits=[9]))
