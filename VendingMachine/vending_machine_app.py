from classes.estoque import Estoque

# Variaveis para estilização:
PRODUTO_STR: str = "PRODUTO"
PRECO_STR: str = "PREÇO"
STOCK_STR: str = "ESTOQUE"

# Instanciamos o Estoque para carregar os produtos do JSON
estoque_maquina = Estoque()

def imprime_item(item):
    print(f"{item.id:<5} {item.nome:<12} {item.preco:<8.2f} {item.quantidade:<10}")

# Função para mostrar a máquina de vendas
def mostrar_maquina():
    print("------------------------------------------------------------------------")
    print(f"ID   {PRODUTO_STR:<12} {PRECO_STR:<8} {STOCK_STR:<10}")
    print("------------------------------------------------------------------------")
    estoque_maquina.listar() # Usamos o método listar do Estoque
    print("------------------------------------------------------------------------")

def calcular_troco(valor_a_pagar):
    cedulas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.5, 0.25, 0.1, 0.01]

    troco_usado = {}

    for cedula in cedulas:
        quantidade = 0
        while valor_a_pagar >= cedula:
            valor_a_pagar -= cedula
            valor_a_pagar = round(valor_a_pagar, 2)
            quantidade += 1
        if quantidade > 0:
            troco_usado[cedula] = quantidade

    for moeda in moedas:
        quantidade = 0
        while valor_a_pagar >= moeda:
            valor_a_pagar -= moeda
            valor_a_pagar = round(valor_a_pagar, 2)
            quantidade += 1
        if quantidade > 0:
            troco_usado[moeda] = quantidade

    return troco_usado

def verificar_stock_e_comprar(item_escolhido):
    if item_escolhido.quantidade > 0:
        print(f"No estoque há {item_escolhido.quantidade} {item_escolhido.nome}.")
        valor_pago = 0.0
        while valor_pago < item_escolhido.preco:
            try:
                entrada_dinheiro = float(input(f"Insira o dinheiro para comprar {item_escolhido.nome} (Preço: R${item_escolhido.preco:.2f}): "))
                valor_pago += entrada_dinheiro
                if valor_pago < item_escolhido.preco:
                    print(f"Faltam R${item_escolhido.preco - valor_pago:.2f}. Insira mais dinheiro.")
            except ValueError:
                print("Por favor, digite um valor numérico válido.")

        if valor_pago >= item_escolhido.preco:
            print("Compra bem-sucedida!")
            troco = valor_pago - item_escolhido.preco
            if troco > 0:
                troco_detalhado = calcular_troco(troco)
                print(f"Seu troco é de R${troco:.2f}.")
                for valor, qtd in sorted(troco_detalhado.items(), reverse=True):
                    tipo = "cédula(s)" if valor >= 2 else "moeda(s)"
                    print(f"  {qtd} x R${valor:.2f} {tipo}")
            else:
                print("Não há troco.")

            # Atualiza o estoque usando o método do Estoque
            estoque_maquina.atualizar_quantidade(item_escolhido.id, item_escolhido.quantidade - 1)
            print(f"Restam {item_escolhido.quantidade} {item_escolhido.nome} no estoque.")
            return True
    else:
        print("Item fora de estoque, por favor selecione outro item.")
        return False

# Função para aguardar a entrada do cliente
def entrada_cliente():
    while True:
        mostrar_maquina()
        try:
            escolha = int(input("Digite o ID do produto que deseja comprar (0 para sair): "))
            if escolha == 0:
                print("Saindo da máquina de vendas.")
                break
            
            item = estoque_maquina.obter_produto_por_id(escolha)
            if item:
                verificar_stock_e_comprar(item)
            else:
                print("ID inválido, tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    entrada_cliente()