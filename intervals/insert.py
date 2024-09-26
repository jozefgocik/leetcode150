# https://leetcode.com/problems/insert-interval/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def insert(self, intervals, newInterval):
    #     result = []
    #     i = 0
    #     while i < len(intervals) and intervals[i][0] < newInterval[0]:
    #         result.append(intervals[i])
    #         i += 1
    #
    #     currentInterval = newInterval
    #     lastInterval = None if not result else result.pop()
    #     if lastInterval is not None:
    #         if lastInterval[1] >= newInterval[0]:
    #             currentInterval = [min(newInterval[0], lastInterval[0]), max(newInterval[1], lastInterval[1])]
    #         else:
    #             result.append(lastInterval)
    #
    #     while i < len(intervals) and currentInterval[1] >= intervals[i][0]:
    #         currentInterval = [min(currentInterval[0], intervals[i][0]), max(currentInterval[1], intervals[i][1])]
    #         i += 1
    #     result.append(currentInterval)
    #
    #     while i < len(intervals):
    #         result.append(intervals[i])
    #         i += 1
    #
    #     return result

    # Solution 2
    # O(n) time / O(n) space
    def insert(self, intervals, newInterval):
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        result.append(newInterval)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    print(solution.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
    print(solution.insert(intervals=[[1, 5]], newInterval=[6, 8]))
