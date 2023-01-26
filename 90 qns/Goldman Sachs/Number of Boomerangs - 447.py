class Solution:
    def point_distance(self, p1, p2):
        return ((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2)

    def boomerang(self, dic):
        result = 0
        for key in dic.keys():
            if key != "0" and dic[key] > 1:
                result = dic[key] * (dic[key] - 1)
        return result

    def numberOfBoomerangs(self, points):
        result = 0
        for i in range(len(points)):
            temp = {}
            for j in range(len(points)):
                dist = str(self.point_distance(points[i], points[j]))
                if dist in temp:
                    temp[dist] += 1
                else:
                    temp[dist] = 1
            result += self.boomerang(temp)
        return result


obj = Solution()

testcases = [[[0, 0], [1, 0], [2, 0]], [[1, 1], [2, 2], [3, 3]], [[1, 1]], [
    [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]]

for t in testcases:
    print("Answer", obj.numberOfBoomerangs(t))
