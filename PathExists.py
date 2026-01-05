from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        q = deque([source])
        seen = {source}

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)

        return False
