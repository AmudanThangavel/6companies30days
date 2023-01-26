from collections import defaultdict as dd


class Solution:

    def topKFrequent(self, words, k):
        freq_words = dd(int)
        for word in words:
            freq_words[word] += 1
        word = list(freq_words.keys())
        freq_words = dict(
            sorted(freq_words.items(), key=lambda item: item[1], reverse=True))
        freq_ls = list(freq_words.values())
        words = list(freq_words.keys())
        freq = sorted(list(set(freq_ls)), reverse=True)
        i = 0
        result = []
        for f in freq:
            temp = []
            while i < len(freq_ls) and freq_ls[i] == f:
                temp.append(words[i])
                i += 1
            temp.sort()
            if len(result) + len(temp) < k:
                result.extend(temp)
            elif len(result) + len(temp) > k:
                result.extend(temp[:k-(len(result) + len(temp))])
            else:
                result.extend(temp)
                break
        return result

        # pass


obj = Solution()
testcase = [[["i", "love", "leetcode", "i", "love", "coding"], 2], [
    ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4], [["i", "love", "leetcode", "i", "love", "coding"], 3]]
for test in testcase:
    print("ANSWER", obj.topKFrequent(test[0], test[1]))
