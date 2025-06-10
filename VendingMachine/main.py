from classes.estoque import Estoque
import getpass
import vending_machine_app

# Login do usuário
adm_user: str = "sergioDoJson"
adm_password: str = "123"

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
            menu_administrador()
            break# Login bem-sucedido
        else:
            print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas - 1 - _}")
    
    print("Número máximo de tentativas excedido. Acesso negado.")
    return False # Login falhou

def menu_administrador():
    estoque = Estoque()
    while True:
        print("\n--- MODO ADMINISTRADOR ---")
        print("[1] Cadastrar produto")
        print("[2] Editar produto")
        print("[3] Remover produto")
        print("[4] Listar produtos")
        print("[0] Sair do modo administrador")

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
            print("Saindo do modo administrador...")
            break
        else:
            print("Opção inválida.")

def menu_principal():
    while True:
        print("\n--- MÁQUINA DE VENDAS ---")
        print("[1] Usar máquina de vendas (Modo Cliente)")
        print("[2] Acessar modo administrador")
        print("[0] Sair do programa")

        escolha_modo = input("Escolha o modo: ")

        if escolha_modo == "1":
            vending_machine_app.entrada_cliente() # Chama a função principal da máquina de vendas
        elif escolha_modo == "2":
            # Aqui você pode adicionar uma autenticação de senha para o administrador
            login()
            if login == True:
             menu_administrador()
           
        elif escolha_modo == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida.")
        
if __name__ == "__main__":
    menu_principal()