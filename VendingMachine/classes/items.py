class Produto:

    def __init__(self,id,nome,preco,quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self): #transforma os items em um dicionario
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        }
    
    @classmethod
    def from_dict(cls,data): #cria um objeto a partir de um dicionario, UTIL para carregar arquivos .json
        return cls(data["id"], data["nome"], data["preco"], data["quantidade"])
    
