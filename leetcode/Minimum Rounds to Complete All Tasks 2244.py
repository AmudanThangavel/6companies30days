from collections import defaultdict as dd


class Solution:
    def minimumRounds(self, tasks):
        rounds = 0
        freq = dd(int)
        for i in tasks:
            freq[i] += 1
        for num in freq.values():
            if num == 1:
                return -1
            elif num == 2:
                rounds += 1
            elif num % 3 == 0:
                rounds += int(num/3)
            elif num % 3 == 1:
                rounds += int(((num - 1) / 3) + 1)
            elif num % 3 == 2:
                rounds += int((num+1) / 3)
            print(num, rounds)
        return rounds


obj = Solution()
testcases = [[2, 2, 3, 3, 2, 4, 4, 4, 4, 4], [2, 3, 3]]
for t in testcases:
    print("Answer", obj.minimumRounds(t))
