def keypad_combinations(digits):
    if not digits:
        return []
    
    keypad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    res = []
    
    def solve(idx, curr):
        if idx == len(digits):
            res.append(curr)
            return
        
        ch = digits[idx]
        
        if ch not in keypad:
            solve(idx + 1, curr)
            return
        
        for letter in keypad[ch]:
            solve(idx + 1, curr + letter)
            
    solve(0, "")
    return res

print(keypad_combinations("13"))
            