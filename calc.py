import os
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

operations={"+":add, "-": sub, "*":mul, "/":div}
n1=int(input("Enter first number : "))
should_continue=True
while should_continue:
    for symbol in operations:
        print(symbol)
    operators=input("Pick one operator from above : ")
    n2=int(input("What's the next number : "))
    result=operations[operators]
    answer=result(n1, n2)
    print(f"{n1} {operators} {n2} = {answer}")
    prompt=input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit : ")
    if prompt=="n":
        should_continue=False
    else:
        os.system("clear")
        print(f"previous answer is '{answer}'")
        n1=answer
        
    





    
