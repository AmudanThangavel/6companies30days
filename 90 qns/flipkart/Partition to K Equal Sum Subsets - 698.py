from functools import cache


class Solution:
    def canPartitionKSubsets(self, nums, k):
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        # n = len(nums)
        used = [False]*len(nums)

        @cache
        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k-1, 0)
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)


obj = Solution()
testcases = [[[4, 3, 2, 3, 5, 2, 1], 4], [
    [1, 2, 3, 4], 3], [[1, 1, 1, 1, 2, 2, 2, 2], 4], [[10, 5, 5, 4, 3, 6, 6, 7, 6, 8, 6, 3, 4, 5, 3, 7], 8], [[2, 9, 4, 7, 3, 2, 10, 5, 3, 6, 6, 2, 7, 5, 2, 4], 7]]
for t in testcases:
    print(obj.canPartitionKSubsets(t[0], t[1]))
