"""
Sistema de Gerenciamento de Biblioteca
Autor: Carlos Henrique Lima Da Silva
Descrição:
Este sistema permite gerenciar livros, usuários e empréstimos
utilizando listas e dicionários em Python.
"""

# ==============================
# Estruturas de Dados
# ==============================

livros = []
usuarios = []
emprestimos = []


# ==============================
# Funções de Livros
# ==============================

def adicionar_livro():
    """Adiciona um novo livro à biblioteca"""
    try:
        titulo = input("Digite o título do livro: ").strip()
        autor = input("Digite o autor do livro: ").strip()

        if not titulo or not autor:
            print("❌ Título e autor não podem ser vazios.")
            return

        livro = {
            "titulo": titulo,
            "autor": autor,
            "disponivel": True
        }

        livros.append(livro)
        print("✅ Livro adicionado com sucesso!")

    except Exception as e:
        print(f"Erro ao adicionar livro: {e}")


def remover_livro():
    """Remove um livro da biblioteca"""
    titulo = input("Digite o título do livro a remover: ").strip()

    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            livros.remove(livro)
            print("✅ Livro removido com sucesso!")
            return

    print("❌ Livro não encontrado.")


def listar_livros():
    """Lista todos os livros da biblioteca"""
    if not livros:
        print("📚 Nenhum livro cadastrado.")
        return

    print("\n📚 Lista de Livros:")
    for livro in livros:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(
            f"- {livro['titulo']} | Autor: {livro['autor']} | Status: {status}")


def pesquisar_livros():
    """Pesquisa livros disponíveis e emprestados"""
    print("\n1 - Livros Disponíveis")
    print("2 - Livros Emprestados")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        encontrados = [l for l in livros if l["disponivel"]]
        print("\n📗 Livros Disponíveis:")
    elif opcao == "2":
        encontrados = [l for l in livros if not l["disponivel"]]
        print("\n📕 Livros Emprestados:")
    else:
        print("❌ Opção inválida.")
        return

    if not encontrados:
        print("Nenhum livro encontrado.")
        return

    for livro in encontrados:
        print(f"- {livro['titulo']} | Autor: {livro['autor']}")


# ==============================
# Funções de Usuários
# ==============================

def registrar_usuario():
    """Registra um novo usuário"""
    nome = input("Digite o nome do usuário: ").strip()

    if not nome:
        print("❌ Nome inválido.")
        return

    usuarios.append(nome)
    print("✅ Usuário registrado com sucesso!")


def listar_usuarios():
    """Lista todos os usuários"""
    if not usuarios:
        print("👤 Nenhum usuário registrado.")
        return

    print("\n👤 Lista de Usuários:")
    for usuario in usuarios:
        print(f"- {usuario}")


# ==============================
# Funções de Empréstimos
# ==============================

def registrar_emprestimo():
    """Registra o empréstimo de um livro"""
    if not livros or not usuarios:
        print("❌ É necessário ter livros e usuários cadastrados.")
        return

    titulo = input("Digite o título do livro: ").strip()
    usuario = input("Digite o nome do usuário: ").strip()

    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            if not livro["disponivel"]:
                print("❌ Livro já está emprestado.")
                return

            if usuario not in usuarios:
                print("❌ Usuário não encontrado.")
                return

            livro["disponivel"] = False
            emprestimos.append({
                "titulo": titulo,
                "usuario": usuario
            })

            print("✅ Empréstimo registrado com sucesso!")
            return

    print("❌ Livro não encontrado.")


def listar_emprestimos():
    """Lista todos os empréstimos"""
    if not emprestimos:
        print("📄 Nenhum empréstimo registrado.")
        return

    print("\n📄 Empréstimos Ativos:")
    for emp in emprestimos:
        print(f"- Livro: {emp['titulo']} | Usuário: {emp['usuario']}")


# ==============================
# Menu Principal
# ==============================

def menu():
    """Exibe o menu do sistema"""
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Adicionar Livro")
    print("2 - Remover Livro")
    print("3 - Mostrar Todos os Livros")
    print("4 - PESQUISAR Livros (Disponíveis / Emprestados)")
    print("5 - Registrar Usuário")
    print("6 - Listar Usuários")
    print("7 - Registrar Empréstimo")
    print("8 - Listar Empréstimos")
    print("9 - Fechar Sistema")


# ==============================
# Execução do Sistema
# ==============================

def main():
    """Função principal do sistema"""
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            remover_livro()
        elif opcao == "3":
            listar_livros()
        elif opcao == "4":
            pesquisar_livros()
        elif opcao == "5":
            registrar_usuario()
        elif opcao == "6":
            listar_usuarios()
        elif opcao == "7":
            registrar_emprestimo()
        elif opcao == "8":
            listar_emprestimos()
        elif opcao == "9":
            print("👋 Sistema encerrado.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


# Inicialização
if __name__ == "__main__":
    main()

# Projeto Gerenciamento de Biblioteca Concluído com sucesso
