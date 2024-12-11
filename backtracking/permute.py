# https://leetcode.com/problems/permutations/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n * n!) time / O(n * n!) space
    def permute(self, nums):
        result = []

        def dfs(currentNums, current):
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(currentNums)):
                current.append(currentNums[i])
                dfs(currentNums[:i] + currentNums[i+1:], current)
                current.pop()

        dfs(nums, [])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute(nums=[1, 2, 3]))
    print(solution.permute(nums=[0, 1]))
    print(solution.permute(nums=[1]))
