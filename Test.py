
listOfOperators=["*","+","^"]
def perform_op(op_stack):
    listOfOperands=[]
    while op_stack[-1] not in listOfOperators:
        listOfOperands.append(op_stack.pop())
    op=op_stack.pop()
    if op == "+":
        res=0
        for i in listOfOperands:
            res+=i
        return res
    elif op == "*":
        res=1
        for i in listOfOperands:
            res*=i
        return res
    elif op == "^":
        listOfOperands.reverse()
        res = listOfOperands[0]
        for i in listOfOperands[1:]:
            res=pow(res,i)
        return res

while True:
    datainput= input()
    datainput+="$"
    op_stack=[]

    curr_token=""

    for c in datainput:
        if c==" ":
            if "add" in curr_token:
                op_stack.append("+")
            elif "multiply" in curr_token:
                op_stack.append("*")
            elif "exponent" in curr_token:
                op_stack.append("^")
            else:
                op_stack.append(int(curr_token))
            curr_token=""
        elif c==")":
            op_stack.append(int(curr_token))

            curr_token=str(perform_op(op_stack))
        elif c=="$":
            op_stack.append(int(curr_token))
        else:
            curr_token+=c

    print(op_stack)
