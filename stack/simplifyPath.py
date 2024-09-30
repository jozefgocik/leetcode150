# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):

    # Solution 1
    # O(n) time / O(n) space
    # def simplifyPath(self, path):
    #     stack = []
    #
    #     dirs = path.split('/')
    #     for directory in dirs:
    #         if directory == '' or directory == '.':
    #             continue
    #         elif directory == '..':
    #             if stack:
    #                 stack.pop()
    #         else:
    #             stack.append(directory)
    #
    #     return '/' + '/'.join(stack)

    # Solution 2
    # O(n) time / O(n) space
    def simplifyPath(self, path):
        stack = []
        current = ""

        for c in path + "/":
            if c == "/":
                if current == "..":
                    if stack:
                        stack.pop()
                elif current != "" and current != ".":
                    stack.append(current)
                current = ""
            else:
                current += c

        return "/" + "/".join(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath(path="/home/"))
    print(solution.simplifyPath(path="/home//foo/"))
    print(solution.simplifyPath(path="/home/user/Documents/../Pictures"))
    print(solution.simplifyPath(path="/../"))
    print(solution.simplifyPath(path="/.../a/../b/c/../d/./"))
