# https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def isHappy(self, n):
        cache = set()
        currentNum = n

        while currentNum not in cache:
            if currentNum == 1:
                return True

            cache.add(currentNum)
            temp = 0
            for num in str(currentNum):
                squaredNum = int(num) * int(num)
                temp += squaredNum

            currentNum = temp

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(n=19))
    print(solution.isHappy(n=2))
