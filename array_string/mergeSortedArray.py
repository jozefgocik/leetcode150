# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # O(n) time / O(1) space
    def merge(self, nums1, m, nums2, n):
        index1 = m - 1
        index2 = n - 1

        for i in reversed(range(0, m + n)):
            if index2 < 0 or (index1 >= 0 and nums1[index1] > nums2[index2]):
                nums1[i] = nums1[index1]
                index1 -= 1
            else:
                nums1[i] = nums2[index2]
                index2 -= 1

        return nums1


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
    print(solution.merge(nums1=[2, 0], m=1, nums2=[1], n=1))
    print(solution.merge(nums1=[0], m=0, nums2=[1], n=1))
