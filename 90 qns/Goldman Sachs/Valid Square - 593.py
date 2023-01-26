class Solution:
    def validSquare(self, p1, p2, p3, p4):
        points = [p1, p2, p3, p4]
        distance = set()
        for i in range(3):
            for j in range(i+1, 4):
                distance.add(((points[i][0] - points[j][0])
                             ** 2) + ((points[i][1] - points[j][1])**2))
        return not 0 in distance and len(distance) == 2


obj = Solution()

testcases = [[[0, 0], [1, 1], [1, 0], [0, 1]],
             [[0, 0], [1, 1], [1, 0], [0, 12]],
             [[1, 0],  [-1, 0], [0, 1], [0, -1]]]

for t in testcases:
    print("Answer", obj.validSquare(t[0], t[1], t[2], t[3]))
