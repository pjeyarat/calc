import sys

def add(operand1, operand2):
    return (int(operand1) + int(operand2))
def multiply(operand1, operand2):
    return (int(operand1) * int(operand2))
alu = {
    "add": add,
    "multiply": multiply
}

def parse(tokens):
    s_expr = [] 
    s_func = []
    for elem in tokens:
        if elem == "(":
            continue
        elif elem == ")":
            if len(s_func) < 1:
                print("malformed input")
                sys.exit(1)
            if len(s_expr) < 2:
                print("malformed input")
                sys.exit(1)
            operation = s_func.pop()
            operand1 = s_expr.pop()
            operand2 = s_expr.pop()
            if operation in alu:
                s_expr.append(alu[operation](operand1, operand2))
            else:
                print("invalid operation")
                sys.exit(1)
        elif elem == "add":
            s_func.append("add")
        elif elem == "multiply":
            s_func.append("multiply")
        else:
            s_expr.append(elem)  
    return s_expr, s_func

def tokenize(inp):
    l = [] #token container list
    i = 0;
    while(i <  len(inp)):
        if inp[i] == "(":
            l.append("(")
            i = i + 1
        elif inp[i] == ")":
            l.append(")")
            i = i + 1
        elif inp[i] == "a":
            s = inp[i:i+3]
            if s != "add":
                print("malformed input")
                sys.exit(1)
            i = i + 3
            l.append("add")
        elif inp[i] == "m":
            s = inp[i:i+8]
            if s != "multiply":
                print("malformed input")
                sys.exit(1)
            i = i + 8
            l.append("multiply")
        elif inp[i] == " ":
            i = i + 1
            continue
        elif inp[i].isdigit():
            num = None
            j = i
            while( j < len(inp) and inp[j].isdigit()):
                if num == None:
                    num = inp[j]
                else:
                    num = num + inp[j]
                j = j + 1
            i = j
            l.append(num)
        else:
            print("malformed input") 
            sys.exit(1)
            break
    return l

def validate(inp):
    return True

def main():
    if len(sys.argv) == 2:
         inp = sys.argv[1]
         if validate(inp):
            tokens = tokenize(inp)
            s_expr, s_func = parse(tokens)
            if len(s_func) != 0:
                print("malformed input detected")
                sys.exit(1)
            if len(s_expr) != 1:
                print("malformed input detected")
                sys.exit(1)
            print(s_expr[0])
    else:
        print("invalid argument")
   
if __name__ == '__main__':
    main()