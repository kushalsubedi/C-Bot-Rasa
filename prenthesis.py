

def check_prenthesis(expression:str)->bool:
    stack = []
    openings = ['(','{','[']

    for bracket in expression:
        if bracket in openings:
            stack.append(bracket)
        else :
            if not stack:
                return False
            if (bracket == ')' and stack[-1] == '(') or (bracket == '}' and stack[-1] == '{') or (bracket == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
    return not stack


x = check_prenthesis("[{}()]")
print(x)