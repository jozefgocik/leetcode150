# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # Solution 1
    # O(n) time / O(n) space
    def candy(self, ratings):
        cache = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                cache[i] = cache[i - 1] + 1

        for i in reversed(range(1, len(ratings))):
            if ratings[i] < ratings[i - 1] and cache[i - 1] <= cache[i]:
                cache[i - 1] = cache[i] + 1

        return sum(cache)


if __name__ == '__main__':
    solution = Solution()
    print(solution.candy(ratings=[1, 0, 2]))
    print(solution.candy(ratings=[1, 2, 2]))
    print(solution.candy(ratings=[1, 0, 2, 3, 5, 4]))
    print(solution.candy(ratings=[1, 2, 87, 87, 87, 2, 1]))
