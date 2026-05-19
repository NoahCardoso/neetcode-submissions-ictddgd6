from queue import Queue
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for num in range(n):
            adj[num] = set()
        for edge in edges:
            s, t = edge[0], edge[1]
            adj[s].add(t)
            adj[t].add(s)
        if n == 1 and len(edges) == 0: return True
        elif n == 1: return False
        # bfs to check connectivity
        q = Queue()
        q.put(0)
        vis = set()
        while q.qsize() > 0:
            curr = q.get()
            if curr in vis:
                continue
            vis.add(curr)
            for num in adj[curr]:
                if num not in vis:
                    q.put(num)
        if len(vis) != len(adj):
            return False
        # then if connected use dfs to check if cycle
        s = []
        s.append(0)
        vis = set()
        while len(s) > 0:
            curr = s.pop()
            if curr in vis:
                return False
            vis.add(curr)
            for num in adj[curr]:
                if num not in vis:
                    s.append(num)
        return True