class Solution:
    def largestDivisibleSubset(self, nums):
        self.dp = []
        return constructLDS(nums, self.dp, getLDS[1])

    def getLDS(self, nums, dp):
        nums = sorted(nums)
        self.dp = [1 for i in range(len(nums))]
        idssize = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    self.dp[i] = max(self.dp[i], self.dp[j] + 1)
                    idssize = max(idssize, self.dp[i])
        return idssize

    def constructLDS(nums, dp, idssize):
        prev = -1
        ids = []


obj = Solution()
testcases = [[1, 2, 3], [1, 2, 4, 8]]
for t in testcases:
    print("Answer", obj.largestDivisibleSubset(t))
