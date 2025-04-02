# https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * m) / O(n) space; n = number of rows, m = number of cols
    # def minimumTotal(self, triangle):
    #     previousRow = triangle[0]
    #
    #     for i in range(1, len(triangle)):
    #         newRow = []
    #         for j in range(len(triangle[i])):
    #             num = triangle[i][j]
    #             if j == 0:
    #                 newRow.append(num + previousRow[0])
    #             elif j == len(previousRow):
    #                 newRow.append(num + previousRow[-1])
    #             else:
    #                 value = min(num + previousRow[j - 1], num + previousRow[j])
    #                 newRow.append(value)
    #
    #         previousRow = newRow
    #
    #     return min(previousRow)

    # Solution 1
    # O(n * m) / O(n) space; n = number of rows, m = number of cols
    def minimumTotal(self, triangle):
        cache = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i in range(len(row)):
                num = row[i]
                cache[i] = num + min(cache[i], cache[i + 1])

        return cache[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(solution.minimumTotal(triangle=[[-10]]))
