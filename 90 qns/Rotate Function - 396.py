class Solution:
    def maxRotateFunction(self, nums):
        pre = 0
        total = 0
        for i, num in enumerate(nums):
            pre += (i*num)
            total += num
        l = len(nums)
        result = pre
        print(pre)
        for i in range(l - 1):
            pre -= total
            pre += nums[i] * l
            result = max(pre, result)
            print(pre)
        return result


obj = Solution()

testcases = [[4, 3, 2, 6], [100], [4, 3, 6]]

for t in testcases:
    print("Answer", obj.maxRotateFunction(t))
