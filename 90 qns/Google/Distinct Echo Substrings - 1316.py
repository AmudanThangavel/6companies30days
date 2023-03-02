class Solution:
    def distinctEchoSubstrings(self, text):
        result = set()
        for i in range(len(text)):
            for j in range(i+1, len(text)):
                if text[i:j] == text[j:j+j-i]:
                    result.add(text[i:j])
        return len(result)


obj = Solution()
testcases = ["abcabcabc", "leetcodeleetcode"]
for test in testcases:
    print("ANSWER", obj.distinctEchoSubstrings(test))
