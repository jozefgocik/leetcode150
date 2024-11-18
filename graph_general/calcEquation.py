# https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    # Solution 1
    # O(n * (e + v)) time / O(e + v) space; e = number of edges, v = number of vertices
    def calcEquation(self, equations, values, queries):
        result = []
        nodes = {}
        for i in range(len(equations)):
            val1, val2 = equations[i]

            if val1 not in nodes:
                nodes[val1] = []
            if val2 not in nodes:
                nodes[val2] = []

            nodes[val1].append([val2, values[i]])
            nodes[val2].append([val1, 1.0 / values[i]])

        for query in queries:
            val1, val2 = query
            if val1 not in nodes or val2 not in nodes:
                result.append(-1)
            else:
                result.append(self.bfs(nodes, val1, val2))

        return result

    def bfs(self, nodes, source, target):
        queue = [[source, 1]]
        visited = set()
        while queue:
            current, val = queue.pop(0)
            visited.add(current)
            for child in nodes[current]:
                if child[0] == target:
                    return val * child[1]
                if child[0] not in visited:
                    queue.append([child[0], val * child[1]])

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                                queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
