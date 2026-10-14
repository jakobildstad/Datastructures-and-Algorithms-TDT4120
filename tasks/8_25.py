from collections import deque

def shortest_road(build_map, start, end):
    height = len(build_map)
    width = len(build_map[0])
    
    # bfs
    queue = deque([start])
    
    visited = [
        [
            False for _ in range(width)
        ] for _ in range(height)
    ]
    visited[start[0]][start[1]] = True
    
    last_pos = [
        [
            None for _ in range(width)
        ] for _ in range(height)
    ]
    
    # helper
    def _build_path(i, j):
        path = [(i, j)]
        while (i, j) != start:
            i, j = last_pos[i][j]
            path.append((i,j))
            
        path.reverse()
        return path
    
    while queue:
        i, j = queue.popleft() 
        
        if (i,j) == end:
            return _build_path(i, j)
            
        candidates = (
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1)
        )
        
        for i_c, j_c in candidates:
            valid_position = i_c < height and j_c < width and i_c >= 0 and j_c >= 0
            if valid_position and build_map[i_c][j_c]:
                if not visited[i_c][j_c]:
                    last_pos[i_c][j_c] = (i, j)
                    queue.append((i_c, j_c))
                    visited[i_c][j_c] = True