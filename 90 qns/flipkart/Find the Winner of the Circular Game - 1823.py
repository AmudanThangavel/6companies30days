class Solution:
    def findTheWinner(self, n, k):
        players = [i for i in range(1, n+1)]
        i = 0
        while len(players) > 1:
            i = (i+k-1) % len(players)
            players.pop(i)
        return players[0]


obj = Solution()
testcases = [[5, 2], [6, 5]]
for t in testcases:
    print("Input", t[0], t[1], "Answer ", obj.findTheWinner(t[0], t[1]))
