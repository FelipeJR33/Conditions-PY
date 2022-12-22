idade = 18
possuiPatologia = False
altura = 150
ehEstudante = True
ingresso = "Pague 10" if ehEstudante else "Pague 20"

if idade < 18 or idade > 65 or altura < 150 or possuiPatologia:
    print("ACESSO NEGADO")
else:
    print(ingresso) 

