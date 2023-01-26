from collections import defaultdict as dd
import heapq


class Solution:
    def networkDelayTime(self, times, nodes, k):
        edges = dd(list)
        for e, n, t in times:
            edges[e].append((n, t))
        print(edges)
        visited = set()
        min_heap = [(0, k)]
        time = 0
        while min_heap:
            delay, edge = heapq.heappop(min_heap)
            if edge in visited:
                continue
            visited.add(edge)
            time = max(time, delay)
            for e, d in edges[edge]:
                if e not in visited:
                    heapq.heappush(min_heap, (delay+d, e))
        print(time)
        print(visited, nodes)
        return time if len(visited) == nodes else -1


obj = Solution()
testcases = [[[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2],
             [[[1, 2, 1]], 2, 1], [[[1, 2, 1]], 2, 2], [[[1, 2, 1], [2, 1, 3]], 2, 2], [[[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1]]
for t in testcases:
    print(obj.networkDelayTime(t[0], t[1], t[2]))
