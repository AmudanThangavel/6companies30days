from collections import defaultdict as dd


class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        secret_dic = dd(int)
        guess_dic = dd(int)
        l = len(secret)
        for i in range(l):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                guess_dic[guess[i]] += 1
                secret_dic[secret[i]] += 1
        # print(secret_dic)
        # print(guess_dic)
        for i in range(26):
            cows += (min(guess_dic[str(i)], secret_dic[str(i)]))
        return f"{bulls}A{cows}B"


obj = Solution()
testcases = [["1807", "7810"], ["1123", "0111"], ["011", "110"]]
for t in testcases:
    print(obj.getHint(t[0], t[1]))
