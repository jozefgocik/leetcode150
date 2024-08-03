# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def reverseWords(self, s):
    #     cache = []
    #
    #     currentWord = ""
    #     for char in s:
    #         if char != " ":
    #             currentWord += char
    #         elif currentWord != "":
    #             cache.append(currentWord)
    #             currentWord = ""
    #
    #     if currentWord != "":
    #         cache.append(currentWord)
    #
    #     return ' '.join(reversed(cache))

    # Solution 2
    # O(n) time / O(n) space
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords(s="the sky is blue"))
    print(solution.reverseWords(s="  hello world  "))
    print(solution.reverseWords(s="a good   example"))
