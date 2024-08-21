# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        result = 1
        for left in range(len(s)):
            cache = set(s[left])
            right = left + 1
            while right < len(s):
                if s[right] in cache:
                    break

                cache.add(s[right])
                right += 1

            result = max(result, right - left)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s="abcabcbb"))
    print(solution.lengthOfLongestSubstring(s="bbbbb"))
    print(solution.lengthOfLongestSubstring(s="pwwkew"))
