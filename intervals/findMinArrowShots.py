# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * log(n)) time / O(1) space
    def findMinArrowShots(self, points):
        result = 0
        points.sort()
        currentEnd = points[0][1]
        for point in points[1:]:
            if point[0] <= currentEnd:
                currentEnd = min(currentEnd, point[1])
            else:
                result += 1
                currentEnd = point[1]

        return result + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(solution.findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(solution.findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))
