def solve_n_queens(n):
    board = [[ "." for _ in range(n)] for _ in range(n)]
    ans = []
    
    def solve(col):
        if col == n:
            ans.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                solve(col + 1)
                board[row][col] = "."
        
        
    def is_safe(row, col):
        # upper left diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r-=1
            c-=1
            
        # left side column
        c = col
        while c >= 0:
            if board[row][c] == "Q":
                return False
            c-=1
            
        # lower left diagonal
        r, c = row, col
        while r < n and c >= 0:
            if board[r][c] == "Q":
                return False
            r+=1
            c-=1
            
        return True
    
    solve(0)
    return ans

print(solve_n_queens(4))
            
        