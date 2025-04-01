## Implementing a CLI Based Calculator that performs basic Arithmatic operation
def calculator():
    while True:
        print("\n---------- Simple Calculator ----------\n")
        print("Following are the Arithmatic Operation you can perform:\n'+','-','*','/' or 'q' to exit.")
        
        op = input("Enter The operation you want to perform:: ")
        if op.lower() == 'q':
            print("Exited...")
            break
        if op not in ['+','-','*','/']:
            print("Enter a valid operation")
            continue
        try:
            n1 = int(input("Enter The first Number:: "))
            n2 = int(input("Enter The Second Number:: "))

            if op == '+':
                result = n1+n2
            elif op == '-':
                result = n1-n2
            elif op == '*':
                result = n1*n2
            elif op == '/':
                if n2 == 0:
                    print(f"Error: {n1} can not be devided with 0. please Enter a valid non zero number.")
                    continue
                result = n1/n2
            print(f"Output::{result}\n ")
            break
        except ValueError:
            print("Invalid input. please Enter valid Numbers")

calculator()