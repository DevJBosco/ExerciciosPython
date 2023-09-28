num1= float(input("Digite um número:"))
num2= float(input("Digite um número:"))
num3= float(input("Digite um número:"))

if num1>num2:
    if num1>num3:
        print(f"{num1} é o maior número:")
elif num2>num3:
    print(f"{num2} é o maior número:")
else:
    print(f"{num3} é o maior número")