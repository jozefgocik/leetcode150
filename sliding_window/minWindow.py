# https://leetcode.com/problems/minimum-window-substring/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(m) space
    # def minWindow(self, s, t):
    #     result = ""
    #
    #     charSet = {}
    #     for char in t:
    #         if char not in charSet:
    #             charSet[char] = 0
    #         charSet[char] += 1
    #
    #     for i in range(len(s)):
    #         currentString = ""
    #         currentCharSet = charSet.copy()
    #         for j in range(i, len(s)):
    #             if s[j] in currentCharSet:
    #                 currentCharSet[s[j]] -= 1
    #                 if currentCharSet[s[j]] <= 0:
    #                     currentCharSet.pop(s[j])
    #
    #             currentString += s[j]
    #
    #             if not currentCharSet:
    #                 result = currentString if (result == "" or len(currentString) < len(result)) else result
    #                 break
    #
    #     return result

    # Solution 2
    # O(n + m) time / O(m) space
    def minWindow(self, s, t):
        if t == "":
            return ""

        countT, window = {}, {}
        for char in t:
            if char not in countT:
                countT[char] = 0
            countT[char] += 1

        have, need = 0, len(countT)
        result, resultLength = [-1, -1], float("inf")
        left = 0
        for right in range(len(s)):
            currentChar = s[right]
            if currentChar not in window:
                window[currentChar] = 0
            window[currentChar] += 1

            if currentChar in countT and window[currentChar] == countT[currentChar]:
                have += 1

            while have == need:
                if right - left + 1 < resultLength:
                    result = [left, right]
                    resultLength = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        return s[result[0]:result[1] + 1] if resultLength != float("inf") else ""


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(solution.minWindow(s="a", t="a"))
    print(solution.minWindow(s="a", t="aa"))
