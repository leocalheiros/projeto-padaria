from src.models.repositories.produto_repository import ProdutoRepository
from src.views.produto_view import ProdutoView


class ProdutoController:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        self.produto_view = ProdutoView()

    def cadastrar_produto(self, nome: str, sabor: str) -> None:
        self.produto_repository.cadastrar_produto(nome, sabor)
        self.produto_view.cadastrar_produto(nome, sabor)

    def listar_todos_produtos(self):
        return self.produto_repository.listar_todos_produtos()

    def deletar_produto(self, nome: str):
        self.produto_repository.deletar_produto(nome)
        self.produto_view.deletar_produto(nome)
