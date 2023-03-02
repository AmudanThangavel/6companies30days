class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        charIndex, output = {'a': -1, 'b': -1, 'c': -1}, 0
        for i in range(len(s)):
            charIndex[s[i]] = i
            output += min(charIndex.values())+1

        return output


obj = Solution()
testcases = ["abcabc", "aaacb", "abc"]
for t in testcases:
    print("Answer", obj.numberOfSubstrings(t))
