#Taschenrechner
a = []
for i in range(4):
    print (i+1, ". Zahl eingeben: ")
    a[i]= int(input())

op = input("Operator eingeben: ")

if op == "+":
    print(a[0] + a[1])
elif op == "-":
    print(a[0] - a[1])
elif op == "*":
    print(a[0] * a[1])
elif op == "/":
    print(a[0] / a[1])

#Implementieren sie einen RPM Taschenrechner mit einer Stackteife von 4
stack = []
op = ["+", "-", "*", "/"]
for i in range(4):
    stack.append(int(input()))
    if stack[i] in op:
        if stack[i] == "+":
            stack[i-2] = stack[i-2] + stack[i-1]
        elif stack[i] == "-":
            stack[i-2] = stack[i-2] - stack[i-1]
        elif stack[i] == "*":
            stack[i-2] = stack[i-2] * stack[i-1]
        elif stack[i] == "/":
            stack[i-2] = stack[i-2] / stack[i-1]
        stack.pop()
        stack.pop()


#vontinue #break
#was passiert wenn ich die in einer Schleife verwende?