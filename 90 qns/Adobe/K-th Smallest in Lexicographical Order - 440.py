class Solution(object):
    def findKthNumber(self, n, k):
        result = 1
        while k > 1:
            count = 0
            interval = [result, result+1]
            while interval[0] <= n:
                count += min(n+1, interval[1]) - interval[0]
                interval = [interval[0]*10, interval[1]*10]
            if k > count:
                k -= count
                result += 1
            else:
                k -= 1
                result *= 10
        return result
