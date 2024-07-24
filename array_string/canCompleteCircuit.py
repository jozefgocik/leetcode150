# https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(1) space
    # def canCompleteCircuit(self, gas, cost):
    #     for i in range(len(gas)):
    #         currentGas = gas[i]
    #         currentCost = cost[i]
    #
    #         if currentGas >= currentCost:
    #             isResult = True
    #             totalGas = 0
    #             for j in range(i, len(gas) + i):
    #                 currentGas = gas[j % len(gas)]
    #                 currentCost = cost[j % len(cost)]
    #                 totalGas += currentGas
    #                 if totalGas >= currentCost:
    #                     totalGas -= currentCost
    #                 else:
    #                     isResult = False
    #                     break
    #
    #             if isResult:
    #                 return i % len(gas)
    #
    #     return -1

    # Solution 2
    # O(n) time / O(1) space
    def canCompleteCircuit(self, gas, cost):
        maxLength = 0
        tank = 0
        for i in range(len(gas) * 2):
            tank += gas[i % len(gas)] - cost[i % len(cost)]
            if tank >= 0:
                maxLength += 1
            else:
                maxLength = 0

            tank = max(tank, 0)

        if maxLength >= len(gas):
            return len(gas) * 2 - maxLength

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
    print(solution.canCompleteCircuit(gas=[5, 8, 2, 8], cost=[6, 5, 6, 6]))
