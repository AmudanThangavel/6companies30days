from functools import cache


class Solution:
    def closedIsland(self, grid):
        result = 0
        closed_island = 0
        self.row, self.col = len(grid), len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == 0:
                    if self.dfs(i, j, grid):
                        result += 1
        return result

    @cache
    def dfs(self, i, j, grid):
        if i >= self.row or j >= self.col or i < 0 or j < 0:
            return False
        if grid[i][j] == 1 or grid[i][j] == -1:
            return True
        grid[i][j] = -1
        island = True
        for i, j in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
            if not self.dfs(i, j, grid):
                island = False
        return island


obj = Solution()
testcases = [
    [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ],
    [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]]
for test in testcases:
    print("ANSWER", obj.closedIsland(test))
