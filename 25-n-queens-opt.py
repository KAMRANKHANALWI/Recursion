def solve_n_queens(n):
    board = [[ "." for _ in range(n)] for _ in range (n)]
    ans = []
    
    leftRow = [0] * n
    lowerDiagonal = [0] * (2 * n - 1)
    upperDiagonal = [0] * (2 * n - 1)
    
    def solve(col):
        if col == n:
            ans.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            if (leftRow[row] == 0 and 
                lowerDiagonal[row + col] == 0 and 
                upperDiagonal[n - 1 + col - row] == 0):
                
                # place
                board[row][col] = "Q"
                leftRow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1
                
                solve(col + 1)
                
                # backtrack
                board[row][col] = "."
                leftRow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0
                
    solve(0)
    return ans

print(solve_n_queens(4))
                
    
    