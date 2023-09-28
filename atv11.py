idade=int(input("Digite a idade:"))
mesatual=int(input("Digite o mes atual :"))
diasnasc=int(input("Digite o dia de nascimento:"))
mesnasc=int(input("Digite o mes de nascimento :"))
dias=int(input("digite o dia que estamos:"))
diasfinal= dias-diasnasc
mesesfinal = mesatual-mesnasc
diastotal= (idade*365)+(mesesfinal*30)+diasfinal
print(f"A quantidade de dias total é {diastotal}")
