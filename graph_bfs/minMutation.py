# https://leetcode.com/problems/minimum-genetic-mutation/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    def minMutation(self, startGene, endGene, bank):
        queue = [[startGene, 0]]
        seen = set()
        while queue:
            current, count = queue.pop(0)
            seen.add(current)
            if current == endGene:
                return count

            for i in range(len(current)):
                choices = ["A", "C", "G", "T"]
                for choice in choices:
                    new = current[0:i] + choice + current[i + 1:]
                    if new in bank and new not in seen:
                        queue.append([new, count + 1])

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"]))
    print(solution.minMutation(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
