# https://leetcode.com/problems/ipo/?envType=study-plan-v2&envId=top-interview-150
import heapq


class Solution(object):

    # Solution 1
    # O(n * log(n)) time / O(n) space
    def findMaximizedCapital(self, k, w, profits, capital):
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)

            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)

        return w


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
    print(solution.findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
