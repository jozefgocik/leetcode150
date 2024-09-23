# https://leetcode.com/problems/merge-intervals/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * log(n)) time / O(n) space
    def merge(self, intervals):
        result = []
        intervals.sort()
        if not intervals:
            return result

        currentInterval = intervals[0]
        for interval in intervals[1:]:
            if currentInterval[1] >= interval[0]:
                currentInterval[1] = max(currentInterval[1], interval[1])
            else:
                result.append(currentInterval)
                currentInterval = interval

        result.append(currentInterval)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solution.merge(intervals=[[1, 4], [4, 5]]))
    print(solution.merge(intervals=[[1, 4], [0, 4]]))
