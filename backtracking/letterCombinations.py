# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(3^n * 4^m) time / O(3^n * 4^m) space
    # def letterCombinations(self, digits):
    #     result = []
    #     letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
    #                "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
    #                "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    #
    #     if not digits:
    #         return result
    #
    #     def dfs(word, currentDigits):
    #         if len(word) == len(digits):
    #             result.append(word)
    #             return
    #
    #         digit = currentDigits[0]
    #         for letter in letters[digit]:
    #             dfs(word + letter, currentDigits[1:])
    #
    #     dfs("", digits)
    #     return result

    # Solution 2
    # O(3^n * 4^m) time / O(3^n * 4^m) space
    def letterCombinations(self, digits):
        if not digits:
            return []

        letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                   "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                   "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        return self.letterCombinationsHelper([], digits, letters, "", 0)

    def letterCombinationsHelper(self, result, digits, letters, word, index):
        if len(word) == len(digits):
            result.append(word)
            return result

        digit = digits[index]
        for letter in letters[digit]:
            result = self.letterCombinationsHelper(result, digits, letters, word + letter, index + 1)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations(digits="23"))
    print(solution.letterCombinations(digits=""))
    print(solution.letterCombinations(digits="2"))
