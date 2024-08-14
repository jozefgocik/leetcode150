# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def isSubsequence(self, s, t):
        sIndex = 0
        tIndex = 0

        while sIndex < len(s) and tIndex < len(t):
            if t[tIndex] == s[sIndex]:
                sIndex += 1
            tIndex += 1

        return sIndex == len(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isSubsequence(s="abc", t="ahbgdc"))
    print(solution.isSubsequence(s="axc", t="ahbgdc"))
