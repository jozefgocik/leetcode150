# https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def canConstruct(self, ransomNote, magazine):
        letters = {}

        for char in ransomNote:
            if char not in letters:
                letters[char] = 0
            letters[char] += 1

        for char in magazine:
            if char in letters:
                letters[char] -= 1
                if letters[char] == 0:
                    letters.pop(char)

        return not letters


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct(ransomNote="a", magazine="b"))
    print(solution.canConstruct(ransomNote="aa", magazine="ab"))
    print(solution.canConstruct(ransomNote="aa", magazine="aab"))
