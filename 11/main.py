# renda mensal do aluno, em centavos.
import math
rendaMensalEmCentavos = 300_999

# Tempo decorrido de contrato. Se for maior que 60 meses, o aluno não deve mais nada.
mesesDecorridos = 13

# Soma das parcelas já pagas pelo aluno nos meses anteriores(em centavos). Se for igual a 18 mil reais, o aluno não deve pagar mais nada, pois já quitou a dívida.
totalJaPagoPeloAluno = 6000

motivo = ""


if rendaMensalEmCentavos < 200000:
    motivo = " Nenhum valor é devido pois a renda do estudante está abaixo do valor mínimo de R$ 2000 reais."
elif mesesDecorridos > 60:
    motivo = " Nenhum valor é devido pois o prazo máximo para pagamento expirou"
else:
    motivo = " Nenhum valor é devido pois a dívida já foi paga"

if rendaMensalEmCentavos < 200000 or mesesDecorridos > 60 or totalJaPagoPeloAluno >= 1800000:
    print("O valor da parcela desse mês é R$ 0 reais." + motivo)
else:
    print(
        f'O valor da parcela desse mês é R$ {round(rendaMensalEmCentavos * 0.0018, 2)} reais')
