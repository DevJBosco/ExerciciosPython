inicio = int(input("Que horas o xadrez começou?:"))
fim = int(input("Que horas o xadrez acabou?:"))
if inicio <= fim:
    total = inicio-fim
else:
   total=(24-inicio)+fim
print(f"A partida  durou {total} horas")