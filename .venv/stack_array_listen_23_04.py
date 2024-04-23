#Taschenrechner
#Implementieren sie einen RPM Taschenrechner mit einer Stackteife von 4

stack = []                              #leere Liste für den Stack

def calc(stack):                        #Funktion für die Berechnung
    if len(stack) == 3:                 #wenn die Länge des Stacks 3 ist
        opperenant = stack.pop()        #dann wird das letzte Element aus dem Stack entfernt und in der Variable opperenant gespeichert
        a = int(stack.pop())            #das nächste Element wird entfernt und in der Variable a gespeichert
        b = int(stack.pop())            #das nächste Element wird entfernt und in der Variable b gespeichert
        if opperenant == "+":           #wenn das Element in opperenant ein "+" ist
            c = a + b                   #dann wird die Summe von a und b in der Variable c gespeichert
        elif opperenant == "-":         #wenn das Element in opperenant ein "-" ist
            c = b - a                   #dann wird die Differenz von b und a in der Variable c gespeichert
        elif opperenant == "*":         #wenn das Element in opperenant ein "*" ist
            c = a * b                   #dann wird das Produkt von a und b in der Variable c gespeichert
        elif opperenant == "/":         #wenn das Element in opperenant ein "/" ist
            c = b / a                   #dann wird der Quotient von b und a in der Variable c gespeichert
        stack.append(c)                 #die Variable c wird in den Stack hinzugefügt

    if len(stack) == 4:                 #wenn die Länge des Stacks 4 ist
        opperenant = stack.pop()
        a = int(stack.pop())
        b = int(stack.pop())
        c = int(stack.pop())
        if opperenant == "+":
            d = a + b + c
        elif opperenant == "-":
            d = c - b - a
        elif opperenant == "*":
            d = a * b * c
        elif opperenant == "/":
            d = c / b / a
        stack.append(d)
    print(stack[0])

for i in range(5):                                  #Schleife für die Eingabe von 5 Zahlen oder Operatoren

    if len(stack) >= 4:                             #wenn die Länge des Stacks größer gleich 4 ist
        print("Stack ist voll")                     #dann wird "Stack ist voll" ausgegeben
        break                                       #und die Schleife wird beendet
    else:                                           #sonst
        print("Zahl oder Operator eingeben: ")      #wird "Zahl oder Operator eingeben: " ausgegeben
        stack.append(input())                       #und die Eingabe wird in den Stack hinzugefügt

    if stack[i] == "+" or stack[i] == "-" or stack[i] == "*" or stack[i] == "/":    #wenn das Element in stack ein Operator ist
        calc(stack)                                                                 #dann wird die Funktion calc aufgerufen
                                                                                    #continue wird in einer Schleife verwendet, um den Rest des Codes zu überspringen
                                                                                    #und den nächsten Schleifendurchlauf zu beginnen.