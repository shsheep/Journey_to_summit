class Solution:
    ret = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        N, M = len(grid), len(grid[0])
        visited = collections.defaultdict(lambda: False)
        
        def bfs(cur_x: int, cur_y: int, tmap: List[List[str]]):
            deq = collections.deque()
            deq.append((cur_x, cur_y))
            self.ret += 1
            while deq:
                kx, ky = deq.popleft()
                for d in range(4):
                    nx = kx + dx[d]
                    ny = ky + dy[d]
                    if visited[(nx, ny)]:
                        continue
                    if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                        continue
                    if tmap[nx][ny] == '1':
                        visited[(nx, ny)] = True
                        deq.append((nx, ny))
        
        for x in range(N):
            for y in range(M):
                if grid[x][y] == '1' and not visited[(x, y)]:
                    visited[(x, y)] = True
                    bfs(x, y, grid)
        return self.ret


# Runtime: 168 ms, faster than 20.70% of Python3 online submissions for Number of Islands.
# Memory Usage: 22.1 MB, less than 5.13% of Python3 online submissions for Number of Islands.
