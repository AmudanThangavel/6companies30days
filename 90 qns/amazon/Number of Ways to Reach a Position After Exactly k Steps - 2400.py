class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:

        val = k + endPos - startPos
        if val < 0 or val & 1:
            return 0
        rightStep = val // 2
        leftStep = k - rightStep
        if leftStep < 0:
            return 0
        return self._nChooseK(leftStep + rightStep, min(leftStep, rightStep))

    def _nChooseK(self, n: int, k: int) -> int:
        kMod = 1_000_000_007

        dp = [1] + [0] * k

        for _ in range(n):
            for j in range(k, 0, -1):
                dp[j] += dp[j - 1]
                dp[j] %= kMod

        return dp[k]
