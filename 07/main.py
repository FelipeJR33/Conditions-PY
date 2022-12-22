aposentada = False
portadoraDeDoenca = False
totalDeRendimentos = 10000000 #emCentavos

if aposentada or portadoraDeDoenca:
    print("ISENTA")
elif totalDeRendimentos <= 2_855_970:
    print("VAZA LEÃO. JÁ TÁ DIFÍCIL SEM VOCÊ")
else :
    print("PEGA LEAO") 