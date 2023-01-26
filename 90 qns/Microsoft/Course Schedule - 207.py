class Solution:
    def canFinish(self, numCourses, prerequisites):
        visited = set()
        pre_req = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            pre_req[course].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if pre_req[course] == []:
                return True

            visited.add(course)
            for pre in pre_req[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            pre_req[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


obj = Solution()
testcases = [[2, [[1, 0]]], [2, [[1, 0], [0, 1]]],
             [4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]]]
for t in testcases:
    print("Answer", obj.canFinish(t[0], t[1]))
