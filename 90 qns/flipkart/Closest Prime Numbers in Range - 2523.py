class Solution:

    def closestPrimes(self, left, right):
        def prime(n):
            if n < 2:
                return False
            for x in range(2, int(n**0.5) + 1):
                if n % x == 0:
                    return False
            return True
        dif = float('inf')
        result = [-1, -1]
        pre = 0
        for i in range(left, right+1):
            if prime(i):
                if pre == 0:
                    pre = i
                elif i - pre < dif:
                    dif = i - pre
                    result = [pre, i]
                    if dif <= 2:
                        return result
                pre = i
        return result


obj = Solution()
testcases = [[10, 19], [4, 6], [19, 31], [
    18, 72], [84084, 407043], [1, 1000000], [639740, 639833], [341663, 815604]]
for t in testcases:
    print("Input", t[0], t[1], "Answer ", obj.closestPrimes(t[0], t[1]))
