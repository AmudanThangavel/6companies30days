class Solution:
    def gcd(self, x, y):
        while y != 0:
            x, y = y, x % y

        return x

    def minOperations(self, nums, numsDivide):
        gcd = numsDivide[0]
        count = 0
        for num in numsDivide[1:]:
            gcd = self.gcd(gcd, num)
        nums.sort()
        for num in nums:
            if gcd % num != 0:
                count += 1
            else:
                return count
        return -1


obj = Solution()
testcases = [[[2, 3, 2, 4, 3], [9, 6, 9, 3, 15]], [[4, 3, 6], [8, 2, 6, 10]]]
for t in testcases:
    print(obj.minOperations(t[0], t[1]))
