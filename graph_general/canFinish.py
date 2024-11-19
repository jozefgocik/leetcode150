# https://leetcode.com/problems/course-schedule/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n + p) time / O(n + p) space; p = number of prerequisites
    def canFinish(self, numCourses, prerequisites):
        nodes = {i: [] for i in range(numCourses)}

        for prerequisite in prerequisites:
            post, pre = prerequisite
            nodes[post].append(pre)

        visited = set()

        def dfs(currentNode):
            if currentNode in visited:
                return False

            visited.add(currentNode)
            for prerequisite in nodes[currentNode]:
                result = dfs(prerequisite)
                if not result:
                    return result
            visited.remove(currentNode)
            nodes[currentNode] = []

            return True

        for node in nodes:
            if node not in visited:
                result = dfs(node)
                if not result:
                    return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(numCourses=2, prerequisites=[[1, 0]]))
    print(solution.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
    print(solution.canFinish(numCourses=4, prerequisites=[[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))
