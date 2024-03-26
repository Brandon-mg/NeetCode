def evalRPN(tokens):
    valid_ops = ["+","-","*","/"]
    num_stack = []
    for i in tokens:
        if i in valid_ops and len(num_stack) > 1:
            n1 = num_stack.pop()
            n2 = num_stack.pop()
            match(i):
                case "+":
                    num_stack.append(n2+n1)
                case "-":
                    num_stack.append(n2-n1)
                case "*":
                    num_stack.append(n2*n1)
                case "/":
                    num_stack.append(int(n2/n1))
                case _:
                    return 0
        elif i.lstrip('-').isdigit():
            num_stack.append(int(i))
        else:
            return 0
    if len(num_stack) == 1:
        return num_stack[0]
    return 0

if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]
    print('tokens = ["2","1","+","3","*"]')
    print(evalRPN(tokens))

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print('tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]')
    print(evalRPN(tokens))