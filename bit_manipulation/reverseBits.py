# https://leetcode.com/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150

class Solution:

    # Solution 1
    # O(1) time / O(1) space
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(n=0b00000010100101000001111010011100))
    print(solution.reverseBits(n=0b11111111111111111111111111111101))
