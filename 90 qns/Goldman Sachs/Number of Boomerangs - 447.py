class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0

        for x1, y1 in points:
            count = collections.defaultdict(int)
            for x2, y2 in points:
                ans += 2 * count[(x1 - x2)**2 + (y1 - y2)**2]
                count[(x1 - x2)**2 + (y1 - y2)**2] += 1

        return ans


obj = Solution()

testcases = [[[0, 0], [1, 0], [2, 0]], [[1, 1], [2, 2], [3, 3]], [[1, 1]], [
    [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]]

for t in testcases:
    print("Answer", obj.numberOfBoomerangs(t))
