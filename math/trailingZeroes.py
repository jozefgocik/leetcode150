# https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def trailingZeroes(self, n):
    #     result = 0
    #     factorial = self.factorial(n)
    #     while factorial > 0 and factorial % 10 == 0:
    #         factorial /= 10
    #         result += 1
    #
    #     return result
    #
    # def factorial(self, n):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return n * self.factorial(n - 1)

    # Solution 2
    # O(log(n)) time / O(1) space
    def trailingZeroes(self, n):
        result = 0
        while n >= 5:
            n //= 5
            result += n

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(n=3))
    print(solution.trailingZeroes(n=5))
    print(solution.trailingZeroes(n=0))
