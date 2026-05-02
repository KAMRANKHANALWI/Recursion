def find_paths(maze):
    n = len(maze)
    res = []
    vis = [[0] * n for _ in range(n)]
    
        # D   L  R   U
    di = [+1, 0, 0, -1]
    dj = [0, -1, +1, 0]
    
    dir = "DLRU"
    
    def solve(i, j, move):
        if i == n-1 and j == n-1:
            res.append(move)
            return
        
        for idx in range(4):
            nexti = i + di[idx]
            nextj = j + dj[idx]
            
            if (0 <= nexti < n and 0 <= nextj < n
                and not vis[nexti][nextj] and maze[nexti][nextj] == 1):
                
                vis[i][j] = 1
                solve(nexti, nextj, move + dir[idx])
                vis[i][j] = 0
                
    if maze[0][0] == 1:
        solve(0, 0, "")
        
    return res

# maze = [
#     [1, 0, 0, 0],
#     [1, 1, 0, 1],
#     [0, 1, 0, 0],
#     [1, 1, 1, 1]
# ]

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

print(find_paths(maze))
