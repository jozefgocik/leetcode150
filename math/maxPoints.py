# https://leetcode.com/problems/max-points-on-a-line/?envType=study-plan-v2&envId=top-interview-150

import math


class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(n) space
    def maxPoints(self, points):
        result = 1

        for x1, y1 in points:
            cache = {}
            for x2, y2 in points:
                dx, dy = x2 - x1, y2 - y1
                if dx == 0 and dy == 0:
                    continue

                g = math.gcd(dx, dy)
                dx /= g
                dy /= g

                if (dx, dy) not in cache:
                    cache[(dx, dy)] = 0

                cache[(dx, dy)] += 1
                result = max(result, cache[(dx, dy)] + 1)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))
    print(solution.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
