from sortedcontainers import SortedList


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        previous_diffs = SortedList()

        result = 0
        for idx, (num1, num2) in enumerate(zip(nums1, nums2)):

            difference = num1-num2
            cmp_value = difference + diff

            if previous_diffs:
                lower = previous_diffs.bisect_right(cmp_value)
                result += lower

            minimal_diff = previous_diffs.add(difference)
        return result


obj = Solution()
testcases = [[[3, 2, 5], [2, 2, 1], 1], [[3, -1], [-2, 2], -1]]
for t in testcases:
    print("Answer", obj.numberOfPairs(t[0], t[1], t[2]))
