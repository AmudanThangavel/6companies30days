class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        mid = len(nums)/2
        if len(nums) % 2 == 0:
            return (nums[int(mid+0.5)] + nums[int(mid-0.5)])/2
        else:
            return nums[int(mid)]
        return nums1, nums2


obj = Solution()
testcases = [[[1, 3], [2]], [[1, 2], [3, 4]]]
for t in testcases:
    print(obj.findMedianSortedArrays(t[0], t[1]))
