# Comentarios servirão para explicar o passo a passo do processo
# importar a classe items
from items import Items

# Variavies pra estilização:
produto: str = "PRODUTO"
preço: str = "PREÇO"
stock: str = "ESTOQUE"



# criando os objetos passando os parametros da nossa nova classe
coke = Items(1,"Coca", 3.75, 2)
coffe = Items(2,"café", 1.25, 100)
monster = Items(3,"Monster", 9.96, 1)
pepsi = Items(4,"Pepsi", 3.67, 5)
redbull= Items(5,"Redbull", 13.99, 2)


# passo 1 armazenar os items da maquina em um dicionário formatado
itemsDict = {
    coke.id: coke,
    coffe.id: coffe,
    monster.id: monster,
    pepsi.id: pepsi,
    redbull.id: redbull
}

def imprimeItem(item):
    print(f"{item.id} {item.name:>6} {item.price:>18.2f} {item.stock:>10}")
    
# Função para mostrar a máquina de vendas, com 2 itens por linha
def mostrar_maquina(itens, itens_por_linha=1):
    lista_itens = list(itens.values())
    print("------------------------------------------------------------------------")
    print(f"ID   {produto:>7}  {preço:>13}  {stock:>13}")
    print("------------------------------------------------------------------------")
    for i in lista_itens:
        imprimeItem(i)
# Para não ter que fazer uma matriz com cada preço, ID, item e estoque. Pesquisar uma maneira de criar uma
# Base de dados acessível no python
def calcular_troco(valorApagar):
    cedulas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.5, 0.25, 0.1, 0.01]
    
    troco_usado = {}  # Para armazenar quantas notas/moedas usamos
    
    # Primeiro as cédulas
    for cedula in cedulas:
        quantidade = 0
        while valorApagar >= cedula:
            valorApagar -= cedula
            valorApagar = round(valorApagar, 2)  # arredondar
            quantidade += 1
        if quantidade > 0:
            troco_usado[cedula] = quantidade

    for moeda in moedas:
        quantidade = 0
        while valorApagar >= moeda:
            valorApagar -= moeda
            valorApagar = round(valorApagar, 2)
            quantidade += 1
        if quantidade > 0:
            troco_usado[moeda] = quantidade

    return troco_usado


    # 3,00 -> valorApagar, 
    # se a cedula for > q o valor a pagar ent subtrair ela

def verficarStock(itemEscolhido):
    print(f"No estoque à {itemEscolhido.stock} {itemEscolhido.name}, {itemEscolhido.price}")
    if itemEscolhido.stock > 0:
        print(f"Compra Bem sucedida!") # se for maior, compra success
        itemEscolhido.stock -= 1 # diminui 1 do stock
        print(f"{itemEscolhido.stock}")
        return True # Retorna TRUE para uma compra bem sucedida 
    elif itemEscolhido.stock <= 0:
        print("item fora de estoque, por favor selecione outro item") 
        return False # retorna falso para uma compra falha


# passo 2 Função para aguardar a entrada do cliente
def entradaCliente():
    while True:
        try:
            escolha = int(input("Digite o ID do produto que deseja comprar (0 para sair): "))
            if escolha == 0:
                print("Saindo da máquina de vendas.")
                break
            if escolha in itemsDict:
                item = itemsDict[escolha]
                verficarStock(item)
                calcular_troco(item.price)
            else:
                print("ID inválido, tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")


if __name__ == "__main__":
    mostrar_maquina(itemsDict)
    entradaCliente()


