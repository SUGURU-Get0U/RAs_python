import json
from pathlib import Path
from .items import Produto

#MEU JSON
ARQUIVO_JSON = Path(__file__).parent / "produtos.json"

class Estoque:
    def __init__(self):
        self.produtos = self.carregar()

    def carregar(self): # carrega os produtos do JSON e converte eles em objetos do tipo PRODUTO
        if Path(ARQUIVO_JSON).exists():
            with open(ARQUIVO_JSON, "r") as f:
                data = json.load(f)
                return [Produto.from_dict(item) for item in data]
        return []

    def salvar(self):
        with open(ARQUIVO_JSON, "w") as f:
            json.dump([produto.to_dict() for produto in self.produtos], f, indent=4)

    def listar(self): # tabela formatada com os produtos
        print(f"{'ID':<5} {'PRODUTO':<12} {'PREÇO':<8} {'QNT':<10}")
        print("-" * 40)
        for p in self.produtos:
            print(f"{p.id:<5} {p.nome:<12} {p.preco:<8.2f} {p.quantidade:<10}")

    def cadastrar(self):
        try:
            novo_id = int(input("Digite o ID do novo produto: "))
            if any(p.id == novo_id for p in self.produtos):
                print("ID já existe. Cadastro cancelado.")
                return
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            qtde = int(input("Quantidade em estoque: "))
            self.produtos.append(Produto(novo_id, nome, preco, qtde))
            self.salvar()
            print("Produto cadastrado com sucesso!")
        except ValueError:
            print("Erro: entrada inválida.")

    def editar(self):
        try:
            id_edit = int(input("Digite o ID do produto a editar: "))
            for produto in self.produtos:
                if produto.id == id_edit:
                    nome = input(f"Novo nome [{produto.nome}]: ") or produto.nome
                    preco = input(f"Novo preço [{produto.preco}]: ")
                    qtde = input(f"Nova quantidade [{produto.quantidade}]: ")

                    produto.nome = nome
                    if preco.strip():
                        produto.preco = float(preco)
                    if qtde.strip():
                        produto.quantidade = int(qtde)

                    self.salvar()
                    print("Produto editado com sucesso!")
                    return
            print("Produto não encontrado.")
        except ValueError:
            print("Erro: entrada inválida.")

    def remover(self):
        try:
            id_remover = int(input("Digite o ID do produto a remover: "))
            self.produtos = [p for p in self.produtos if p.id != id_remover]
            self.salvar()
            print("Produto removido com sucesso.")
        except ValueError:
            print("Erro: entrada inválida.")
