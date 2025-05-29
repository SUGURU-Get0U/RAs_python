# Comentarios servirão para explicar o passo a passo do processo

# passo 1 armazenar os items da maquina em uma matriz

itemsMaquina = [["Coca Cola"]["Café"],
                ["Monster"]["Pepsi"],
                ["RedBull"]["sair"]]

# Para não ter que fazer uma matriz com cada preço, ID, item e estoque. Pesquisar uma maneira de criar uma
# Base de dados acessível no python
# Pode ser com MySql ou PostGresSSql tb.

# passo 2 Função para aguardar a entrada do cliente
def entradaCliente(escolhaDoCliente):
    # receber o código inserido pelo cliente
    # validar o código
    while escolhaDoCliente in itemsMaquina:
        pass
        # Caso invalido, solicitar outro valor
        if escolhaDoCliente not in itemsMaquina:
            return False # pensando em um sistema boleano onde se o item estiver na base de dados, a função retornará True senão retorna False

    # Buscar na base de dados o item solicitado pelo cliente

        # Informar o valor a ser pago
def valor_a_Pagar():
    pass