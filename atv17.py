maça= int(input("Quantas maçãs foram compradas?"))
if maça >= 12:
    valorfinal= maça * 1.00
elif maça < 12:
    valorfinal = maça * 1.30
print(f"O valor total de maçãs a ser pago é R${valorfinal}")