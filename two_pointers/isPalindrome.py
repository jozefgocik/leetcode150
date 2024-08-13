# https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if self.isAlphaNum(s[left]) and self.isAlphaNum(s[right]):
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                    continue
                else:
                    return False

            left += 1 if not self.isAlphaNum(s[left]) else 0
            right -= 1 if not self.isAlphaNum(s[right]) else 0

        return True

    def isAlphaNum(self, s):
        return s.isalpha() or s.isdigit()


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(solution.isPalindrome(s="race a car"))
    print(solution.isPalindrome(s=" "))
