class Solution:
    def longestPrefix(self, s):
        i = 0
        lps = [0]
        j = 1
        while j < len(s):
            if s[j] == s[i]:
                i += 1
                lps.append(i)
                j += 1
            else:
                if i != 0:
                    i = lps[i - 1]
                else:
                    lps.append(i)
                    j += 1
        return s[:lps[-1]]


obj = Solution()
testcases = ["level", "ababab"]
for t in testcases:
    print(obj.longestPrefix(t))
