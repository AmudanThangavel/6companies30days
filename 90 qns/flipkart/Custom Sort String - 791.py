class Solution:
    def customSortString(self, order, s):
        from collections import defaultdict as dd
        no_arr = ""
        freq = dd(int)
        for i in s:
            if i not in order:
                no_arr += i
            else:
                freq[i] += 1
        result = ""
        for i in order:
            if i in freq:
                result += i*freq[i]
        result += no_arr

        return result


obj = Solution()
testcases = [["cba", "abcd"], ["cbafg", "abcd"]]
for t in testcases:
    print(obj.customSortString(t[0], t[1]))
