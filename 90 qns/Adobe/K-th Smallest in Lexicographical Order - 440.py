class Solution:
    def findKthNumber(self, n, k):
        if n < 10:
            return k
        dic = {i: 1 for i in range(1, 10)}


obj = Solution()
testcases = [[13, 2], [1, 1], [47, 23]]
for t in testcases:
    print(obj.findKthNumber(t[0], t[1]))
