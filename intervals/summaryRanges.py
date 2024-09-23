# https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def summaryRanges(self, nums):
        result = []
        if not nums:
            return result

        currentPair = [None, None]
        for num in nums:
            if currentPair[0] is None:
                currentPair = [num, num]
            elif currentPair[1] + 1 == num:
                currentPair[1] = num
            else:
                rangeStr = str(currentPair[0]) if currentPair[0] == currentPair[1] else str(currentPair[0]) + "->" + str(currentPair[1])
                result.append(rangeStr)
                currentPair = [num, num]

        rangeStr = str(currentPair[0]) if currentPair[0] == currentPair[1] else str(currentPair[0]) + "->" + str(currentPair[1])
        result.append(rangeStr)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
    print(solution.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
