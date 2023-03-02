class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(k: int, n: int, s: int, path: List[int]) -> None:
            if k == 0 and n == 0:
                ans.append(path)
                return
            if k == 0 or n < 0:
                return

            for i in range(s, 10):
                dfs(k - 1, n - i, i + 1, path + [i])

        dfs(k, n, 1, [])
        return ans


obj = Solution()
testcases = [[3, 7], [4, 9], [4, 1]]
for t in testcases:
    print("Answer", obj.combinationSum3(t[0], t[1]))
