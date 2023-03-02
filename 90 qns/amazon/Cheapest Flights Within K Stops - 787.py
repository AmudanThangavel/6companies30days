class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        pq, graph = [(0, src, 0)], collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        while pq:
            total, src, stops = heapq.heappop(pq)
            if src == dst:
                return total
            if stops > K:
                continue
            for dest, cost in graph[src].items():
                heapq.heappush(pq, (total+cost, dest, stops+1))
        return -1
