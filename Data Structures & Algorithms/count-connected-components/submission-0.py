from queue import Queue
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        vis = set()
        adj = dict()
        for i in range(n):
            adj[i] = set()
        for e in edges:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        def bfs(node):
            q = Queue()
            q.put(node)
            while q.qsize() > 0:
                curr = q.get()
                vis.add(curr)
                for num in adj[curr]:
                    if num not in vis:
                        q.put(num)
        for i in range(n):
            if i not in vis:
                count += 1
            last = len(vis)
            bfs(i)
            if len(vis) == n:
                break
        return count
