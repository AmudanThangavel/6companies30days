class Solution:
    def sortArray(self, nums):
        if len(nums) == 1:
            return nums

        def divide(arr):
            if len(arr) < 2:
                return arr
            middle = len(arr)//2
            left_arr = divide(arr[:middle])
            right_arr = divide(arr[middle:])
            return conquer(left_arr, right_arr)

        def conquer(left, right):
            if not left:
                return right
            if not right:
                return left
            result = []
            l = r = 0
            while len(result) < len(left) + len(left):
                if left[l] <= right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                if l == len(left):
                    result += right[r:]
                    break
                if r == len(right):
                    result += left[l:]
                    break
            return result
        return divide(nums)


obj = Solution()
testcases = [[5, 2, 3, 1], [5, 1, 1, 2, 0, 0]]
for test in testcases:
    print("ANSWER ", obj.sortArray(test))
