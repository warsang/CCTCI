def countPar(string):
    stack = []
    length = 0
    for char in string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            #Pop from stack
            if len(stack) >= 1:
                length += 2
                stack = stack[:-1]
            else:
                pass
    return length

print(countPar('((())'))
            
