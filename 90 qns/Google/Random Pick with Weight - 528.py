class Solution:

    def __init__(self, w: List[int]):
        self.w_cum = []
        self.sum = 0
        for i in w:
            self.sum += i
            self.w_cum.append(self.sum)

    def pickIndex(self) -> int:
        idx = random.randint(1, self.sum)
        return self.binarySearch(idx)

    def binarySearch(self, val):
        l = 0
        r = len(self.w_cum) - 1
        while l < r:
            mid = int(l+(r-l)/2)
            if self.w_cum[mid] < val:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
