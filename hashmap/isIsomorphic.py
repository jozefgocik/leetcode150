# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def isIsomorphic(self, s, t):
    #     if len(s) != len(t):
    #         return False
    #
    #     cache = {}
    #     seen = set()
    #     for i in range(len(s)):
    #         sChar = s[i]
    #         tChar = t[i]
    #         if sChar not in cache:
    #             if tChar in seen:
    #                 return False
    #             cache[sChar] = tChar
    #             seen.add(tChar)
    #         elif cache[sChar] != tChar:
    #             return False
    #
    #     return True

    # Solution 2
    # O(n) time / O(n) space
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        cacheS, cacheT = {}, {}
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if (sChar in cacheS and cacheS[sChar] != tChar) or (tChar in cacheT and cacheT[tChar] != sChar):
                return False

            cacheS[sChar] = tChar
            cacheT[tChar] = sChar

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic(s="egg", t="add"))
    print(solution.isIsomorphic(s="foo", t="bar"))
    print(solution.isIsomorphic(s="paper", t="title"))
