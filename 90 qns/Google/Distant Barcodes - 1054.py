class Solution:
    def rearrangeBarcodes(self, barcodes):
        if len(barcodes) == 1:
            return barcodes
        from collections import defaultdict as dd
        freq = dd(int)
        for i in barcodes:
            freq[i] += 1
        result = []
        num1, num2 = 0, 0
        while len(result) < len(barcodes):
            if num1 <= 0 and len(freq) > 0:
                if len(freq) == 1:
                    key_max = list(freq.keys())[0]
                else:
                    key_max = max(freq, key=lambda x: freq[x])
                num1 = freq.pop(key_max)
            if num2 <= 0 and len(freq) > 0:
                if len(freq) == 1:
                    key_min = list(freq.keys())[0]
                else:
                    key_min = max(freq, key=lambda x: freq[x])
                num2 = freq.pop(key_min)
            if num1 > 0:
                result.append(key_max)
                num1 -= 1
            if num2 > 0:
                result.append(key_min)
                num2 -= 1

        return result


obj = Solution()
testcases = [[1, 1, 1, 2, 2, 2], [1, 1, 1, 1, 2, 2, 3, 3],
             [1, 1, 2], [0], [7, 7, 7, 8, 5, 7, 5, 5, 5, 8]]
for test in testcases:
    print("ANSWER", obj.rearrangeBarcodes(test))
