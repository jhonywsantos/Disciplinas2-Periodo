Codigo = ['Cód 1', 'Cód 2', 'Cód 3', 'Cód 4']
Preço_unidade = [5.30, 6.0, 3.20, 2.50]
produto = []

for i in range(4):
    tupla = (Codigo[i], Preço_unidade[i])
    produto.append(tupla)

while True:
    try:
        usuario = int(input('Digite o número do produto que deseja (1 a 4) ou digite 0 para encerrar: '))
        if usuario == 0:
            print("Programa encerrado. Obrigado por utilizar!")
            break
        elif 1 <= usuario <= 4:
            quantidade = int(input('Digite quantas vezes você quer este produto: '))
            preço_a_ser_pago = produto[usuario - 1][1] * quantidade
            if quantidade >= 15:
                preço_a_ser_pago *= 0.85
            if preço_a_ser_pago >= 40:
                preço_a_ser_pago *= 0.85
            print(f"Preço a ser pago: R${preço_a_ser_pago:.2f}")
        else:
            print("Número de produto inválido. Digite um número entre 1 e 4 ou 0 para encerrar.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
