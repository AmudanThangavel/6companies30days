class Solution:
    def trailingZeroes(self, n):
        result = n // 5
        n = n // 5
        while n > 5:
            result += n // 5
            n = n // 5
        result += n // 5
        return result


obj = Solution()
testcases = [3, 5, 0, 30, 100, 49, 200, 625]
for t in testcases:
    print("Answer", obj.trailingZeroes(t))
