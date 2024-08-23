# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) time / O(n) space
    def findSubstring(self, s, words):
        result = []

        wordSet = {}
        for word in words:
            if word not in wordSet:
                wordSet[word] = 0
            wordSet[word] += 1

        wordLength = len(words[0])
        wordsLength = len(words) * wordLength
        for i in range(len(s) - wordsLength + 1):
            currentWordSet = wordSet.copy()
            currentIndex = i
            currentWord = s[currentIndex:currentIndex + wordLength]
            while currentWord in currentWordSet:
                currentWordSet[currentWord] -= 1
                if currentWordSet[currentWord] <= 0:
                    currentWordSet.pop(currentWord)
                currentIndex += wordLength
                if currentIndex >= len(s):
                    break
                currentWord = s[currentIndex:currentIndex + wordLength]

            if not currentWordSet:
                result.append(i)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
    print(solution.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
    print(solution.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
