while True:
    num=int(input("Digite um número: "))
    escolha=int(input("Digite 1 para antecessor,2 para sucessor e 3 para encerrar o programa: "))
    if escolha == 1:
        print(num-1)
    elif escolha == 2:
        print(num+1)
    else:
        print("Programa encerrado!")
        break