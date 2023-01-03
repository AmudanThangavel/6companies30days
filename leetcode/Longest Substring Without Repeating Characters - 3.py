class Solution:
    def lengthOfLongestSubstring(self, s):
        charaters = set()
        result = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in charaters:
                charaters.add(s[j])
                j += 1
            else:
                charaters.remove(s[i])
                i += 1
            result = max(result, len(charaters))
        return result


obj = Solution()
testcases = ["abcabcbb", "bbbbb"]
for t in testcases:
    print(obj.lengthOfLongestSubstring(t))
