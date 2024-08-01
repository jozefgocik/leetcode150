# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(1) space
    def lengthOfLastWord(self, s):
        result = 0
        for i in reversed(s):
            if i == " " and result != 0:
                break
            result += 1 if i != " " else 0

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord(s="Hello World"))
    print(solution.lengthOfLastWord(s="   fly me   to   the moon  "))
    print(solution.lengthOfLastWord(s="luffy is still joyboy"))
