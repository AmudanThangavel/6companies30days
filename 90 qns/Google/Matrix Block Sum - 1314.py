class Solution:
    def printMatrix(self, matrix, name):
        print("Printing", name, "... .. .")
        for i in matrix:
            print(i)

    def matrixBlockSum(self, mat, k):
        self.printMatrix(mat, "Matrix")
        lmat = len(mat)
        lsmat = len(mat[0])

        sumMatrix = [[0 for i in range(lsmat)] for i in range(lmat)]
        result = [[0 for i in range(lsmat)] for i in range(lmat)]
        for i in range(lmat):
            for j in range(lsmat):
                start, end = max(0, j - k), min(j + k, lsmat-1)
                # Optimize this block
                temp = sum(mat[i][start:end+1])
                sumMatrix[i][j] = temp
                result[i][j] = temp
        for i in range(lmat):
            for j in range(lsmat):
                start, end = max(0, i - k), min(i+k, lmat-1)
                temp = 0
                for x in range(start, end+1):
                    temp += sumMatrix[x][j]
                result[i][j] = temp
        return result


obj = Solution()
testcases = [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1],
             [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2]]
for test in testcases:
    obj.printMatrix(obj.matrixBlockSum(test[0], test[1]), "Result")
