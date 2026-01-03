import gbiblioteca


def setup_function():
    """
    Executado antes de cada teste.
    Limpa os dados para evitar interferência entre testes.
    """
    gbiblioteca.livros.clear()
    gbiblioteca.usuarios.clear()
    gbiblioteca.emprestimos.clear()


def test_adicionar_livro(monkeypatch):
    """
    Testa a função de adicionar livro
    """
    entradas = iter(["Dom Casmurro", "Machado de Assis"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    gbiblioteca.adicionar_livro()

    assert len(gbiblioteca.livros) == 1
    assert gbiblioteca.livros[0]["titulo"] == "Dom Casmurro"
    assert gbiblioteca.livros[0]["autor"] == "Machado de Assis"
    assert gbiblioteca.livros[0]["disponivel"] is True


def test_registrar_usuario(monkeypatch):
    """
    Testa o registro de usuário
    """
    monkeypatch.setattr("builtins.input", lambda _: "Henrique")

    gbiblioteca.registrar_usuario()

    assert len(gbiblioteca.usuarios) == 1
    assert "Henrique" in gbiblioteca.usuarios


def test_registrar_emprestimo(monkeypatch):
    """
    Testa o empréstimo de um livro disponível para um usuário cadastrado
    """

    # Arrange (preparação do teste)
    gbiblioteca.livros.append({
        "titulo": "O Hobbit",
        "autor": "J. R. R. Tolkien",
        "disponivel": True
    })

    gbiblioteca.usuarios.append("Ana")

    entradas = iter(["O Hobbit", "Ana"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act (execução da função testada)
    gbiblioteca.registrar_emprestimo()

    # Assert (verificações)
    assert gbiblioteca.livros[0]["disponivel"] is False
    assert len(gbiblioteca.emprestimos) == 1
    assert gbiblioteca.emprestimos[0]["titulo"] == "O Hobbit"
    assert gbiblioteca.emprestimos[0]["usuario"] == "Ana"
