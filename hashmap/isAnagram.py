# https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def isAnagram(self, s, t):
        cache = {}

        for char in s:
            if char not in cache:
                cache[char] = 0
            cache[char] += 1

        for char in t:
            if char not in cache:
                return False

            cache[char] -= 1
            if cache[char] == 0:
                cache.pop(char)

        return not cache


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram(s="anagram", t="nagaram"))
    print(solution.isAnagram(s="rat", t="car"))
