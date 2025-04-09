# https://leetcode.com/problems/longest-palindromic-substring/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 3) time / O(n) space
    # def longestPalindrome(self, s):
    #     result = s[0]
    #     for i in range(len(s)):
    #         current = s[i]
    #         for j in range(i + 1, len(s)):
    #             current += s[j]
    #             if current == current[::-1]:
    #                 result = current if len(current) > len(result) else result
    #
    #     return result

    # Solution 2
    # O(n ^ 2) time / O(n) space
    def longestPalindrome(self, s):
        result = ""

        for i in range(len(s)):
            odd = self.longestPalindromeHelper(s, i - 1, i + 1)
            result = odd if len(odd) > len(result) else result

            even = self.longestPalindromeHelper(s, i, i + 1)
            result = even if len(even) > len(result) else result

        return result

    def longestPalindromeHelper(self, s, l, r):
        left, right = l, r
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1

        current = s[left + 1:right]
        return current


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome(s="babad"))
    print(solution.longestPalindrome(s="cbbd"))
