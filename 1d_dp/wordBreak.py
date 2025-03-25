# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(2 ^ n) time / O(n) space
    # def wordBreak(self, s, wordDict):
    #     if s == "":
    #         return True
    #
    #     result = False
    #     prefix = ""
    #     for i in range(len(s)):
    #         prefix += s[i]
    #         if prefix in wordDict:
    #             result = self.wordBreak(s[i+1:], wordDict)
    #         if result:
    #             return True
    #
    #     return result

    # Solution 2
    # O(n ^ 2) time / O(n) space
    # def wordBreak(self, s, wordDict):
    #     cache = {}
    #
    #     def dfs(current):
    #         nonlocal cache
    #         if current in cache:
    #             return cache[current]
    #         if current == "":
    #             return True
    #
    #         result = False
    #         prefix = ""
    #         for i in range(len(current)):
    #             prefix += current[i]
    #             if prefix in wordDict:
    #                 result = dfs(current[i + 1:])
    #             if result:
    #                 return True
    #
    #         cache[current] = result
    #         return result
    #
    #     return dfs(s)

    # Solution 3
    # O(n * m) time / O(n) space
    def wordBreak(self, s, wordDict):
        cache = [False for _ in range(len(s) + 1)]
        cache[len(s)] = True

        for i in reversed(range(len(s))):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:
                    cache[i] = cache[i+len(word)]
                if cache[i]:
                    break

        return cache[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(solution.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
