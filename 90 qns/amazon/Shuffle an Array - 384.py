class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.copy = nums[:]
        self.l = len(self.nums)

    def reset(self) -> List[int]:
        self.nums = self.copy[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(self.l):
            a = randint(i, self.l-1)
            self.nums[i], self.nums[a] = self.nums[a], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
