# https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * log(n)) time / O(1) space
    # def hIndex(self, citations):
    #     citations.sort()
    #     hIndex = 0
    #
    #     for i in range(len(citations)):
    #         if hIndex > len(citations) - i:
    #             break
    #
    #         hIndex = min(citations[i], len(citations) - i)
    #
    #     return hIndex

    # Solution 2
    # O(n) time / O(n) space
    def hIndex(self, citations):
        temp = [0 for _ in range(len(citations) + 1)]
        length = len(citations)

        for citation in citations:
            if citation >= length:
                temp[length] += 1
            else:
                temp[citation] += 1

        hIndex = length
        sumTemp = temp[hIndex]
        while hIndex > sumTemp:
            hIndex -= 1
            sumTemp += temp[hIndex]

        return hIndex


if __name__ == '__main__':
    solution = Solution()
    print(solution.hIndex(citations=[3, 0, 6, 1, 5]))
    print(solution.hIndex(citations=[1, 3, 1]))
    print(solution.hIndex(citations=[3, 4]))
    print(solution.hIndex(citations=[1, 3]))
