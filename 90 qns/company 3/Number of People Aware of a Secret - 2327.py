class Solution:
    def spread(self, n):

        pass

    def peopleAwareOfSecret(self, n, delay, forget):
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        start = 0
        for i in range(1, n):
            start = i - delay
            for j in range(stop):
                pass


obj = Solution()

testcases = [[6, 2, 4], [4, 1, 3], ]

for t in testcases:
    print("Answer", obj.peopleAwareOfSecret(t[0], t[1], t[2]))
