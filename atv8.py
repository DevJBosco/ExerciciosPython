soma = 0
vezes= int(input("Digite a quantidade de numeros que serão inseridos:"))
for x in range (vezes):
    num= float(input("Digite um número:"))
    soma = soma+num
media=soma/vezes
print(soma)
print(f"A média foi: {media}")
