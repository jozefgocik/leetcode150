# https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def myPow(self, x, n):
    #     if n == 0:
    #         return 1
    #     elif n < 0:
    #         return 1/x * self.myPow(x, n + 1)
    #     else:
    #         return x * self.myPow(x, n - 1)

    # Solution 2
    # O(log(n)) time / O(log(n)) space
    def myPow(self, x, n):
        result = self.myPowHelper(x, abs(n))
        return result if n >= 0 else 1/result

    def myPowHelper(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        remainder = 1 if n % 2 == 0 else x
        result = self.myPowHelper(x, n//2)

        return result * result * remainder


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(x=2.00000, n=10))
    print(solution.myPow(x=2.10000, n=3))
    print(solution.myPow(x=2.00000, n=-2))
