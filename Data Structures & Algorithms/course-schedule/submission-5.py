class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = dict()
        for num in range(numCourses):
            adj[num] = set()
        for edge in prerequisites:
            a,b = edge[0], edge[1]
            adj[a].add(b)
        
        def hasCycle(adj):
            visited = set()
            path = set()

            def dfs(node):
                # Node already in current DFS path -> cycle
                if node in path:
                    return True

                # Already fully processed
                if node in visited:
                    return False

                visited.add(node)
                path.add(node)

                for neighbor in adj[node]:
                    if dfs(neighbor):
                        return True

                # Remove when backtracking
                path.remove(node)

                return False

            for node in adj:
                if dfs(node):
                    return True

            return False
        return not hasCycle(adj)