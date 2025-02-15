# https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    # def isPalindrome(self, x):
    #     return str(x) == str(x)[::-1]

    # Solution 2
    # O(n) time / O(1) space
    def isPalindrome(self, x):
        if x < 0:
            return False

        y, temp = 0, x
        while temp > 0:
            y *= 10
            y += temp % 10
            temp //= 10

        return x == y


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(x=121))
    print(solution.isPalindrome(x=-121))
    print(solution.isPalindrome(x=10))
