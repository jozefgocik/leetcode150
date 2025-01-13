# https://leetcode.com/problems/median-of-two-sorted-arrays/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # Solution 1
    # O(log(min(n, m))) time / O(n + m) space
    def findMedianSortedArrays(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            leftA = A[i] if i >= 0 else float("-inf")
            rightA = A[i + 1] if i < len(A) - 1 else float("inf")
            leftB = B[j] if j >= 0 else float("-inf")
            rightB = B[j + 1] if j < len(B) - 1 else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return min(rightA, rightB)
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                right = i - 1
            else:
                left = i + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
