class Solution:
    def maxConsecutive(self, bottom, top, special):
        if not special:
            return (bottom - top) + 1
        special.sort()
        start = bottom
        result = 0
        for relax in special:
            result = max((relax - start), result)
            start = relax + 1
        result = max(top - relax, result)
        return result


obj = Solution()
testcases = [[2, 9, [4, 6]], [6, 8, [7, 6, 8]]]
for test in testcases:
    print(obj.maxConsecutive(test[0], test[1], test[2]))
