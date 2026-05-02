def generate_parentheses(n):
    result = []
    
    def solve(open, close, curr):
        if len(curr) == 2*n:
        # if open == n and close == n:
            result.append(curr)
            return
        
        if open < n:
            solve(open + 1, close, curr + "(")
            
        if close < open:
            solve(open, close + 1, curr + ")")
            
    solve(0, 0, "")
    return result

print(generate_parentheses(4))
