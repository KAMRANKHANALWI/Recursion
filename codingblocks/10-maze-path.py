"""
# ? Find all possible paths from the top-left corner (1,1) 
# ? to the bottom-right corner (n,n) of an n*n grid, moving only 
# ? right (Horizontal) or down (Vertical).
# ? For n=3, the grid is 3*3 and you start at (1,1), end at (3,3).

# ## Input / Output
# * Input: n = 3 (grid size)
# * Output: All paths as strings of 'V' (down) and 'H' (right)
VVHH
VHVH
VHHV
HVVH
HVHV
HHVV
# ~ Total paths = C(2*(n-1), n-1). For n=3 → C(4,2) = 6 paths. 
# ~ You always take exactly (n-1) V moves and (n-1) H moves.
"""

def maze_path(n, row, col, ans):
    if row == n and col == n:
        print(ans)
        return
    
    if row > n or col > n:
        return
    
    # maze_path(n, row + 1, col, ans + "D")
    # maze_path(n, row, col + 1, ans + "R")
    maze_path(n, row + 1, col, ans + "V")
    maze_path(n, row, col + 1, ans + "H")
    
maze_path(3, 1, 1, "")