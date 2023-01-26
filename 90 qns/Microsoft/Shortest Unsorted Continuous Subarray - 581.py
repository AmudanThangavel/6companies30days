class Solution:
    def findUnsortedSubarray(self, nums):
        temp = sorted(nums)
        # if temp == nums:
        #     return 0
        l = len(nums)
        start = -1
        end = - 1
        for i in range(l):
            if temp[i] != nums[i] and start == -1:
                start = i
            if temp[-i-1] != nums[-i-1] and end == -1:
                end = l - i
            if end != -1 and start != -1:
                break
        return end - start


obj = Solution()
testcases = [[2, 6, 4, 8, 10, 9, 15], [1, 2, 3, 4], [1], [2, 1]]
for t in testcases:
    print("Answer", obj.findUnsortedSubarray(t))
