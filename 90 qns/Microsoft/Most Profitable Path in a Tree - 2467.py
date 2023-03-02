class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        def iter_dfs():
            lookup = [[float("-inf"), float("inf")] for _ in range(len(adj))]
            stk = [(1, (0, -1, 0))]
            while stk:
                step, (u, p, ah) = stk.pop()
                if step == 1:
                    stk.append((2, (u, p, ah)))
                    for v in adj[u]:
                        if v == p:
                            continue
                        stk.append((1, (v, u, ah+1)))
                elif step == 2:
                    if len(adj[u])+(u == 0) == 1:
                        lookup[u][0] = 0
                    if u == bob:
                        lookup[u][1] = 0
                    for v in adj[u]:
                        if v == p:
                            continue
                        lookup[u][0] = max(lookup[u][0], lookup[v][0])
                        lookup[u][1] = min(lookup[u][1], lookup[v][1])
                    if ah == lookup[u][1]:
                        lookup[u][0] += amount[u]//2
                    elif ah < lookup[u][1]:
                        lookup[u][0] += amount[u]
                    lookup[u][1] += 1
            return lookup[0][0]

        adj = [[] for _ in range(len(edges)+1)]
        lookup = [False]*len(adj)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()
