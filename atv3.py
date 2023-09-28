idade = int(input("Digite a idade:"))
ano = int(input("Digite o ano atual ou desejado:"))
mesnasc= int(input("Digite o mes de nascimento de 1 a 12:"))
mesatual= int(input("Digite o mes atual de 1 a 12:"))
if mesnasc>mesatual:
    nasc = ano - idade - 1
else:
    nasc = ano - idade
print(f"o ano de nascimento foi {nasc}")
