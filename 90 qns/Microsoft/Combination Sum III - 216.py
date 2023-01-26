class Solution:
    def dfs(self, k, n, i, ls, res):
        pass

    def combinationSum3(self, k, n):
        result = []
        ls = [i for i in range(1, k+1)]
        ind = [1 for i in range(k)]
        s = sum(ls)
        if s < n:
            return []
        elif s == n:
            return[ls]
        for i in range(ls[-1]+1, 10):
            ls[-1] = i
            s += 1
            if s == n:
                result.append(ls)
            print(ls)

        i = k - 2
        while i > 0:
            res = self.dfs(k, n, i, ls, [])
            for r in res:
                result.append(r)
            i -= 1

            pass
        return result


obj = Solution()
testcases = [[3, 7], [4, 9], [4, 1]]
for t in testcases:
    print("Answer", obj.combinationSum3(t[0], t[1]))
