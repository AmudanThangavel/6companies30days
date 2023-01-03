class Solution:
    def minDeletionSize(self, strs):
        count = 0
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in range(len(strs)):
                if ord(strs[j][i]) < ord(letter):
                    count += 1
                    # print(j, i, letter, strs[j][i])
                    break
                letter = strs[j][i]
        return count


obj = Solution()
testcases = [["abc", "bce", "cae"], ["cba", "daf", "ghi"],
             ["a", "b"], ["rrjk", "furt", "guzm"]]
for t in testcases:
    print(obj.minDeletionSize(t))
