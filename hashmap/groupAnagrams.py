# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * log(n)) time / O(n) space
    # def groupAnagrams(self, strs):
    #     cache = {}
    #
    #     for word in strs:
    #         sortedWord = "".join(sorted(word))
    #         if sortedWord not in cache:
    #             cache[sortedWord] = []
    #         cache[sortedWord].append(word)
    #
    #     return list(cache.values())

    # Solution 2
    # O(n * m) time / O(n) space; m = avg length of each word
    def groupAnagrams(self, strs):
        cache = {}

        for word in strs:
            key = [0] * 26  # a...z

            for char in word:
                key[ord(char) - ord("a")] += 1

            strKey = str(key)
            if strKey not in cache:
                cache[strKey] = []
            cache[strKey].append(word)

        return list(cache.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams(strs=[""]))
    print(solution.groupAnagrams(strs=["a"]))
