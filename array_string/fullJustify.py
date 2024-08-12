# https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def fullJustify(self, words, maxWidth):
        result = []
        currentLine = []
        currentLength = 0

        i = 0
        while i < len(words):
            if currentLength + len(currentLine) + len(words[i]) > maxWidth:
                leftSpaces = maxWidth - currentLength

                j = 0
                while leftSpaces > 0:
                    j = 0 if len(currentLine) <= 1 else j % (len(currentLine) - 1)
                    currentLine[j] += " "
                    leftSpaces -= 1
                    j += 1

                result.append("".join(currentLine))
                currentLine = []
                currentLength = 0

            currentLine.append(words[i])
            currentLength += len(words[i])
            i += 1

        lastLine = " ".join(currentLine)
        while len(lastLine) < maxWidth:
            lastLine += " "
        result.append(lastLine)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
    print(solution.fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
    print(solution.fullJustify(
        words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
               "Art", "is", "everything", "else", "we", "do"], maxWidth=20))
