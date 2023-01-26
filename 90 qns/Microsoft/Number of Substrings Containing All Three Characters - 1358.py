class Solution:
    def check(self, freq):
        for i in range(freq.values()):
            pass

    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        l = len(s)
        if l == 3:
            return 1
        one = 0
        two = 1
        s = set()
        freq = {"a": 0, "b": 0, "c": 0}
        while two < l:
            pass


obj = Solution()
testcases = ["abcabc", "aaacb", "abc"]
for t in testcases:
    print("Answer", obj.numberOfSubstrings(t))
