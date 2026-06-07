def smart_calculator():
    print("====================================")
    print(" LOGIC GRIND SMART CALCULATOR ")
    print("====================================")
    print("Type 'exit' anytime to quit the program.\n")
    
    while True:
        # 1. Pipili ng operation ang user
        operation = input("Pumili ng operation (+, -, *, /) o i-type ang 'exit': ").strip().lower()
        
        # Pag-check kung gustong lumabas ng user
        if operation == 'exit':
            print("\nGrind never stops. See you sa susunod na session, boss!")
            break
            
        # Input Validation para sa operation
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation! Pumili lang sa +, -, *, o /.\n")
            continue
            
        # 2. Input Validation para sa mga numero gamit ang try-except
        try:
            num1 = float(input("Ipasok ang unang numero: "))
            num2 = float(input("Ipasok ang pangalawang numero: "))
        except ValueError:
            print("Error: Letra o invalid character ang na-input mo. Numero lang dapat, lods!\n")
            print("====================================\n")
            continue
            
        # 3. Pag-compute at Error Handling para sa Zero Division
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error: Bawal mag-divide sa zero! Masisira ang logic ng universe.\n")
                print("====================================\n")
                continue
                
        # Ipapalabas ang pinal na sagot
        print(f"\nResulta: {num1} {operation} {num2} = {result}")
        print("====================================\n")

if __name__ == "__main__":
    smart_calculator()
