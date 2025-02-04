# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150
import heapq


class Solution(object):

    # Solution 1
    # O(n * m + k * log(n * m))) time / O(n * m) space
    # def kSmallestPairs(self, nums1, nums2, k):
    #     nodes = [(i + j, [i, j]) for i in nums1 for j in nums2]
    #     heapq.heapify(nodes)
    #
    #     result = []
    #     for i in range(k):
    #         result.append(heapq.heappop(nodes)[1])
    #
    #     return result

    # Solution 2
    # O(min(k*log(k), m*n*log(m*n))) time / O(min(k, n*m)) space
    def kSmallestPairs(self, nums1, nums2, k):
        result = []
        heap = []
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited = {(0, 0)}

        while len(heap) > 0 and k > 0:
            total, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if i < len(nums1) and j < len(nums2) - 1 and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            if i < len(nums1) - 1 and j < len(nums2) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            k -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
    print(solution.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
    print(solution.kSmallestPairs(nums1=[1, 1, 2], nums2=[0], k=3))
