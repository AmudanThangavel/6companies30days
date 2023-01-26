class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        return 0.5


obj = Solution()
testcases = [1, 2, 3, 4, 5]
for t in testcases:
    print(obj.nthPersonGetsNthSeat(t))
