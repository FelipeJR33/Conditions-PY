# tipo de pagamento dinheiro, credito, debito, cheque.
tipoDePagamento = "cheque"

# valor da mercadoria centavos
valorDoProduto = 13000

valorComDesconto = 2

if tipoDePagamento == "credito":
    valorComDesconto = valorDoProduto * 0.0095
elif tipoDePagamento == "cheque":
    valorComDesconto = valorDoProduto * 0.0097
else:
    valorComDesconto = valorDoProduto * 0.009


print(f'Valor a ser pago: R${round(valorComDesconto,2)}')
