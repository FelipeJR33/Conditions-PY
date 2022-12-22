# valor do produto comprado.
valorDoProduto = 50000

# quantidade de parcelas
quantidadeDoParcelamento = 10

# valor pago
valorPago = 300

valorDaParcela = valorDoProduto * 0.01 / quantidadeDoParcelamento
parcelasPagas = valorPago / valorDaParcela

print(
    f'Restam {int(quantidadeDoParcelamento - parcelasPagas)} parcelas de R${valorDaParcela}')
