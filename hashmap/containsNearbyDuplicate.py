# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def containsNearbyDuplicate(self, nums, k):
        cache = {}
        for i, num in enumerate(nums):
            if num in cache and abs(cache[num] - i) <= k:
                return True
            cache[num] = i

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
    print(solution.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
    print(solution.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
