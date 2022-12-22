jogada1 = "pedra"
jogada2 = "papel"

if jogada1 == jogada2 :
    print("Deu empate")
elif jogada1 == "tesoura" and jogada2 == "papel" :
    print("A jogada 1 ganhou")
elif jogada1 == "pedra" and jogada2 == "tesoura":
    print("A jogada 1 ganhou")
elif jogada1 == "papel" and jogada2 == "pedra":
    print("A jogada 1 ganhou")
elif jogada2 == "tesoura" and jogada1 == "papel":
    print("A jogada 2 ganhou")
elif jogada2 == "pedra" and jogada1 == "tesoura":
    print("A jogada 2 ganhou")
elif jogada2 == "papel" and jogada1 == "pedra":
    print("A jogada 2 ganhou")
else :
    print("Ao menos uma das entradas parece não ser válida. Verifique se as entradas foram de fato 'pedra', 'papel' ou 'tesoura' ") 