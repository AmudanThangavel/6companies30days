class Solution:
    def minDeletionSize(self, strs):
        count = 0
        letter = strs[0][0]
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if ord(strs[j][i]) < ord(letter):
                    count += 1
                    print(j, i, strs[j][i])
                    break
                letter = strs[j][i]
        return count


obj = Solution()
testcases = [["abc", "bce", "cae"], ["cba", "daf", "ghi"], ["a", "b"]]
for t in testcases:
    print(obj.minDeletionSize(t))
