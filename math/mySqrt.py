# https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(log(n)) time / O(1) space
    def mySqrt(self, x):
        left, right = 0, x
        result = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            squared = mid * mid
            if squared < x:
                left = mid + 1
                result = mid
            elif squared > x:
                right = mid - 1
            else:
                return mid

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(x=4))
    print(solution.mySqrt(x=8))
