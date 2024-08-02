# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    # def longestCommonPrefix(self, strs):
    #     result = strs[0]
    #
    #     for i in range(1, len(strs)):
    #         temp = ""
    #         for j in range(min(len(result), len(strs[i]))):
    #             if result[j] == strs[i][j]:
    #                 temp += result[j]
    #             else:
    #                 break
    #
    #         result = temp
    #
    #         if result == "":
    #             break
    #
    #     return result

    # Solution 2
    # O(n) time / O(1) space
    def longestCommonPrefix(self, strs):
        result = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(strs=["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(strs=["dog", "racecar", "car"]))
