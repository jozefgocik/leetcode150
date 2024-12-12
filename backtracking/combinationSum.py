# https://leetcode.com/problems/combination-sum/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def combinationSum(self, candidates, target):
        result = []

        def dfs(newCandidates, current):
            if sum(current) == target:
                result.append(current.copy())
                return
            elif sum(current) > target or len(newCandidates) == 0:
                return

            current.append(newCandidates[0])
            dfs(newCandidates, current)
            current.pop()
            dfs(newCandidates[1:], current)

        dfs(candidates, [])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum(candidates=[2, 3, 6, 7], target=7))
    print(solution.combinationSum(candidates=[2, 3, 5], target=8))
    print(solution.combinationSum(candidates=[2], target=1))
