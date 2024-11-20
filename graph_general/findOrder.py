# https://leetcode.com/problems/course-schedule-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n + p) time / O(n + p) space; p = number of prerequisites
    def findOrder(self, numCourses, prerequisites):
        nodes = {i: [] for i in range(numCourses)}

        for prerequisite in prerequisites:
            post, pre = prerequisite
            nodes[post].append(pre)

        result = []
        visited = set()
        added = set()

        def dfs(current):
            if current in visited:
                return False

            visited.add(current)
            for prerequisite in nodes[current]:
                if not dfs(prerequisite):
                    return False

            if current not in added:
                result.append(current)
                added.add(current)
            visited.remove(current)
            nodes[current] = []
            return True

        for node in nodes:
            if not dfs(node):
                return []

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(numCourses=2, prerequisites=[[1, 0]]))
    print(solution.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
    print(solution.findOrder(numCourses=1, prerequisites=[]))
    print(solution.findOrder(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
