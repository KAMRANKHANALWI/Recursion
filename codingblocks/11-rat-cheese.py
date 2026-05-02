flag = False

def rat_cheese(cr, cc, n, m, ans, maze):
    global flag

    # Base case: reached destination
    if cr == n-1 and cc == m-1 and maze[cr][cc] != 'X':
        flag = True
        ans[cr][cc] = 1
        display(ans)
        return

    # Pruning: out of bounds or wall or already visited
    if cr < 0 or cr >= n or cc < 0 or cc >= m or maze[cr][cc] == 'X':
        return

    # Mark current cell
    ans[cr][cc] = 1
    maze[cr][cc] = 'X'        # visited — block it

    # Try all 4 directions
    rat_cheese(cr+1, cc, n, m, ans, maze)  # down
    rat_cheese(cr, cc+1, n, m, ans, maze)  # right
    rat_cheese(cr-1, cc, n, m, ans, maze)  # up
    rat_cheese(cr, cc-1, n, m, ans, maze)  # left

    # Unmark (backtrack)
    ans[cr][cc] = 0
    maze[cr][cc] = 'O'        # unvisit — let other paths use it

def display(arr):
    for row in arr:
        print(' '.join(map(str, row)))

# --- driver ---
n, m = 4, 4
grid = [
    "OOOX",
    "XOXO",
    "OOXX",
    "XOOO"
]
maze = [list(row) for row in grid]
ans  = [[0]*m for _ in range(n)]

rat_cheese(0, 0, n, m, ans, maze)
if not flag:
    print("NO PATH FOUND")