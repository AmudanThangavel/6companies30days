class Solution:
    def hasAllCodes(self, s, k):
        binary = set()
        for i in range(len(s)-k + 1):
            binary.add(s[i:i+k])
        return True if len(binary) == 1 << k else False


obj = Solution()
testcases = [["00110110", 2], ["0110", 1], ["0110", 2]]
for t in testcases:
    print(obj.hasAllCodes(t[0], t[1]))
