resp = "s"
while resp=="s":
    num1= float(input("Digite um número"))
    num2= float(input("Digite um número"))
    if num1>num2:
        print(f"{num2},{num1}")
    elif num1<num2:
        print(f"{num1},{num2}")
    else:
        print("Valores iguais não serão aceitos")
    resp = input("Deseja recomeçar o codigo? s/n:")
print("fechando o programa!")