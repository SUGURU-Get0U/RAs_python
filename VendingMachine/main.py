from classes.estoque import Estoque
import getpass

# Login do usuário
adm_user: str = "sergioDoJson"
adm_password: str = "bananilsonfarofa3" 
def login():
    """Realiza o processo de login para o modo administrador."""
    print("\n=== LOGIN ADMINISTRADOR ===")
    tentativas = 3 # Limite de tentativas para evitar força bruta simples

    for _ in range(tentativas):
        username = input("Usuário: ")
        # getpass.getpass() é ótimo para senhas, pois não ecoa o que o usuário digita
        password = getpass.getpass("Senha: ")

        if username == adm_user and password == adm_password:
            print("Login bem-sucedido! Acesso ao modo administrador.")
            return True # Login bem-sucedido
        else:
            print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas - 1 - _}")
    
    print("Número máximo de tentativas excedido. Acesso negado.")
    return False # Login falhou


def menu():
    estoque = Estoque()

    while True:
        print("\n=== MODO ADMINISTRADOR ===")
        print("[1] Cadastrar produto")
        print("[2] Editar produto")
        print("[3] Remover produto")
        print("[4] Listar produtos")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            estoque.cadastrar()
        elif opcao == "2":
            estoque.editar()
        elif opcao == "3":
            estoque.remover()
        elif opcao == "4":
            estoque.listar()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    login()
    menu()