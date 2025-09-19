def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def is_operand(ch):
    return ch.isalnum()


def infix_to_postfix(expression):
    stack = []  
    result = "" 
    for ch in expression:
       
        if is_operand(ch):
            result += ch

       
        elif ch == '(':
            stack.append(ch)

       
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop() 

       
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                result += stack.pop()
            stack.append(ch)

  
    while stack:
        result += stack.pop()

    return result



if __name__ == "__main__":
    exp = input("Enter infix expression: ")
    print("Postfix expression:", infix_to_postfix(exp))
