caractere = "5"


if caractere == "A" or caractere == "E" or caractere == "I" or caractere == "O" or caractere == "U":
    print("Vogal maiúscula")
elif caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u":
    print("Vogal minúscula")
elif int(caractere):
    print("Número")
else:
    print("consoante")
