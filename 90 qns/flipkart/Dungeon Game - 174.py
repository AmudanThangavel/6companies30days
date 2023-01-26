from functools import cache


class Solution:
    def calculateMinimumHP(self, dungeon):
        ls = []

        @cache
        def nextpath(path):
            pass


obj = Solution()
testcases = [[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], [[0]]]
for test in testcases:
    print(obj.calculateMinimumHP(test))
