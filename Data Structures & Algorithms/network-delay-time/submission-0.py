class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        minHeap = [(0, k)]
        vis = set()
        res = 0
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in vis:
                continue
            vis.add(v1)
            res = max(res, w1)
            for v2, w2 in edges[v1]:
                if v2 not in vis:
                    heapq.heappush(minHeap, (w2+w1,v2))
        
        return res if len(vis) == n else -1