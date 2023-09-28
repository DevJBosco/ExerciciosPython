eleitores = int(input("Digite a quantidade de eleitores"))
branco = int(input("Digite a quantidade de votos brancos"))
nulo = int(input("Digite a quantidade de votos nulos"))
valido = int(input("Digite a quantidade de votos válidos"))
brancof=branco/eleitores * 100
nulof=nulo/eleitores * 100
validof=valido/eleitores * 100

print(f"Ao total foram {eleitores} eleitores, {branco} votos brancos, {nulo} votos nulos e {valido} votos validos")
print(f"Dentre esse total, {brancof}% foram brancos, {nulof}% foram nulos e {validof}% foram válidos")