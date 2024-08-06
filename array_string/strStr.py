# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(m) space
    # def strStr(self, haystack, needle):
    #     for i in range(len(haystack) - len(needle) + 1):
    #         for j in range(len(needle)):
    #             if haystack[i + j] != needle[j]:
    #                 break
    #             if j == len(needle) - 1:
    #                 return i
    #
    #     return -1

    # Solution 2
    # O(n * m) time / O(m) space
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr(haystack="sasad", needle="sad"))
    print(solution.strStr(haystack="leetcode", needle="leeto"))
