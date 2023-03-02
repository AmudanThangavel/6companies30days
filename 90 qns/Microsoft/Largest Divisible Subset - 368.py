class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        nums = sorted(nums, reverse=False)
        dp = [1 for i in range(0, len(nums))]
        cnt = -1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
            cnt = max(cnt, dp[i])
        res = []
        pivot = -1
        for i in range(len(nums)-1, -1, -1):
            if dp[i] == cnt and (pivot == -1 or pivot % nums[i] == 0):
                pivot = nums[i]
                res.append(nums[i])
                cnt -= 1

        return res


obj = Solution()
testcases = [[1, 2, 3], [1, 2, 4, 8]]
for t in testcases:
    print("Answer", obj.largestDivisibleSubset(t))
