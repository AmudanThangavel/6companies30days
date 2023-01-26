# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        return self.arr[index]

    def length(self):
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, marr: 'MountainArray') -> int:
        def binarySearchleft(low, high):
            while low < high:
                mid = int((low+high)/2)
                if marr.get(mid) < target:
                    low = mid + 1
                elif marr.get(mid) > target:
                    high = mid
                elif marr.get(mid) == target:
                    return mid
            return -1

        def binarySearchright(low, high):
            while low <= high:
                mid = int((low + high) / 2)
                if marr.get(mid) > target:
                    low = mid + 1
                elif marr.get(mid) < target:
                    high = mid - 1
                else:
                    return mid
            return -1

        def peak():
            low = 0
            high = l - 1
            result = low
            while low < high:
                mid = int((low+high)/2)
                if marr.get(mid) < marr.get(mid+1):
                    low = mid + 1
                    result = low
                else:
                    high = mid
            return result

        l = marr.length()
        p = peak()
        left = binarySearchleft(0, p)
        print(marr.get(p))
        if left != -1:
            return "left", left
        right = binarySearchright(p, l-1)
        return "right", right


obj = Solution()
testcases = [[3, [1, 2, 3, 4, 5, 3, 1]], [
    3, [0, 1, 2, 4, 2, 1]], [2, [1, 5, 2]], [2, [1, 2, 3, 4, 5, 3, 1]]]
for t in testcases:
    marr = MountainArray(t[1])
    print("Input", t[0], t[1], "Answer ", obj.findInMountainArray(t[0], marr))
