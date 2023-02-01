class Solution:
    def totalFruit(self, fruits):
        if len(fruits) < 3:
            return 2
        count = 0
        types = []
        for fr in fruits:
            if fr not in types:
                if len(set(types)) == 2:
                    i, temp = len(types) - 1, types[-1]
                    count = max(len(types), count)
                    while types[i] == temp:
                        i -= 1
                    types = types[i+1:]
            types.append(fr)
            count = max(count, len(types))
        return count


obj = Solution()
testcases = [[1, 2, 1], [0, 1, 2, 2], [1, 2, 3, 2, 2],
             [1, 0, 3, 4, 3], [1, 0, 1, 4, 1, 4, 1, 2, 3]]
for test in testcases:
    print(obj.totalFruit(test))
