# https://leetcode.com/problems/number-of-1-bits/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(log(n)) time / O(1) space
    def hammingWeight(self, n):
        result = 0
        while n > 0:
            if n % 2 != 0:
                result += 1
            n = n // 2

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(n=11))
    print(solution.hammingWeight(n=128))
    print(solution.hammingWeight(n=2147483645))
