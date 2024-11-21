# https://leetcode.com/problems/snakes-and-ladders/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n ^ 2) time / O(n ^ 2) space
    def snakesAndLadders(self, board):
        n = len(board)
        queue = [(1, 0)]
        visited = {}

        while queue:
            square, count = queue.pop(0)

            if square == n * n:
                return count

            for i in range(square + 1, min(square + 6, n * n) + 1):
                row, col = self.getCoordinates(i, n)
                if (row, col) in visited and visited[(row, col)] <= count + 1:
                    continue

                visited[(row, col)] = count + 1
                if board[row][col] == -1:
                    queue.append((i, count + 1))
                else:
                    queue.append((board[row][col], count + 1))

        return -1

    def getCoordinates(self, square, n):
        row, col = n - ((square - 1) // n) - 1, (square - 1) % n
        if row % 2 != (n - 1) % 2:
            col = n - col - 1
        return row, col


if __name__ == '__main__':
    solution = Solution()
    print(solution.snakesAndLadders(
        board=[[-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, 35, -1, -1, 13, -1],
               [-1, -1, -1, -1, -1, -1],
               [-1, 15, -1, -1, -1, -1]]))
    print(solution.snakesAndLadders(
        board=[[-1, -1],
               [-1, 3]]))
