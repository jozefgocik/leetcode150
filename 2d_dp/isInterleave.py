# https://leetcode.com/problems/interleaving-string/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(n * m) space
    # def isInterleave(self, s1, s2, s3):
    #     cache = {}
    #     if len(s1) + len(s2) != len(s3):
    #         return False
    #
    #     def dfs(index1, index2):
    #         if index1 == len(s1) and index2 == len(s2):
    #             return True
    #         if (index1, index2) in cache:
    #             return cache[(index1, index2)]
    #
    #         result = False
    #         if index1 < len(s1) and s1[index1] == s3[index1 + index2]:
    #             if dfs(index1 + 1, index2):
    #                 return True
    #         if index2 < len(s2) and s2[index2] == s3[index1 + index2]:
    #             if dfs(index1, index2 + 1):
    #                 return True
    #
    #         cache[(index1, index2)] = result
    #         return result
    #
    #     return dfs(0, 0)

    # Solution 2
    # O(n * m) time / O(n * m) space
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        cache = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        cache[len(s1)][len(s2)] = True

        for i in reversed(range(len(s1) + 1)):
            for j in reversed(range(len(s2) + 1)):
                if i < len(s1) and s1[i] == s3[i + j] and cache[i + 1][j]:
                    cache[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and cache[i][j + 1]:
                    cache[i][j] = True

        return cache[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(solution.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    print(solution.isInterleave(s1="", s2="", s3=""))
