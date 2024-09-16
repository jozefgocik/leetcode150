# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def wordPattern(self, pattern, s):
        sList = s.split()
        if len(pattern) != len(sList):
            return False

        pMap, sMap = {}, {}
        for i in range(len(pattern)):
            pChar = pattern[i]
            sChar = sList[i]

            if (pChar in pMap and pMap[pChar] != sChar) or (sChar in sMap and sMap[sChar] != pChar):
                return False
            pMap[pChar] = sChar
            sMap[sChar] = pChar

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordPattern(pattern="abba", s="dog cat cat dog"))
    print(solution.wordPattern(pattern="abba", s="dog cat cat fish"))
    print(solution.wordPattern(pattern="aaaa", s="dog cat cat dog"))
