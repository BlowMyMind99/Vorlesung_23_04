#Taschenrechner
#Implementieren sie einen RPM Taschenrechner mit einer Stackteife von 4


stack = []

for i in len(stack+1):

    if len(stack) >= 4:
        print("Stack ist voll")
        break
    else:
        print(i+1, ". Zahl eingeben: ")
        stack.append(input())

    if stack[i] == "+":
        print()
    elif stack[i] == "-":
        print(stack[0] - stack[1])

    elif stack[i] == "*":
        print(stack[0] * stack[1])

    elif stack[i] == "/":
        print(stack[0] / stack[1])


def add(self):
    if len(self.stack) >= 2:
        a = self.pop()
        b = self.pop()
        self.push(a+b)
#continue #break
#was passiert wenn ich die in einer Schleife verwende?