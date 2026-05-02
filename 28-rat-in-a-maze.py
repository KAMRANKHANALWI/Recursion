def find_paths(maze):
    n = len(maze)
    res = []
    vis = [[0] * n for _ in range(n)]

    def solve(i, j, move):
        if i == n - 1 and j == n - 1:
            res.append(move)
            return

        # down
        if i + 1 < n and not vis[i + 1][j] and maze[i + 1][j] == 1:
            vis[i + 1][j] = 1
            solve(i + 1, j, move + "D")
            vis[i + 1][j] = 0

        # left
        if j - 1 >= 0 and not vis[i][j - 1] and maze[i][j - 1] == 1:
            vis[i][j - 1] = 1
            solve(i, j - 1, move + "L")
            vis[i][j - 1] = 0

        # right
        if j + 1 < n and not vis[i][j + 1] and maze[i][j + 1] == 1:
            vis[i][j + 1] = 1
            solve(i, j + 1, move + "R")
            vis[i][j + 1] = 0

        # up
        if i - 1 >= 0 and not vis[i - 1][j] and maze[i - 1][j] == 1:
            vis[i - 1][j] = 1
            solve(i - 1, j, move + "U")
            vis[i - 1][j] = 0

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
