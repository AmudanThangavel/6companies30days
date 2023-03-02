class Solution:
    def findIntegers(self, n: int) -> int:
        if n < 2:
            return n + 1

        bits = bin(n).replace('0b', '')
        bits = bits[::-1]
        k = len(bits)

        f = [0] * k
        f[0] = 1
        f[1] = 2
        for i in range(2, k):
            f[i] = f[i - 1] + f[i - 2]

        ans = 0
        for i in range(k - 1, -1, -1):
            if bits[i] == '1':
                ans += f[i]
                if i < k - 1 and bits[i + 1] == '1':
                    return ans

        ans += 1
        return ans
