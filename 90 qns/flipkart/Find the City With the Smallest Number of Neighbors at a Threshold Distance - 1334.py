class Solution:
    def findTheCity(self, n: int, edge_list: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for n1, n2, weight in edge_list:
            dist[n1][n2] = weight
            dist[n2][n1] = weight

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        min_city = -1
        min_value = float('inf')
        for i in range(n):
            value = sum(dist[i][j] <= distanceThreshold for j in range(n))
            if value <= min_value:
                min_value = value
                min_city = i
        return min_city
