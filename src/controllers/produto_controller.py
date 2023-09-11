from src.models.repositories.produto_repository import ProdutoRepository
from src.models.repositories.loja_repository import LojaRepository
from src.views.produto_view import ProdutoView


class ProdutoController:
    def __init__(self):
        self.produto_repository = ProdutoRepository()
        self.loja_repository = LojaRepository()
        self.produto_view = ProdutoView()

    def cadastrar_produto(self, nome: str, sabor: str, loja: str) -> None:
        self.produto_repository.cadastrar_produto(nome, sabor, loja)
        self.produto_view.cadastrar_produto(nome, sabor, loja)

    def listar_todos_produtos(self):
        produtos = self.produto_repository.listar_todos_produtos()
        self.produto_view.mostrar_produtos(produtos)

    def deletar_produto(self, nome: str):
        self.produto_repository.deletar_produto(nome)
        self.produto_view.deletar_produto(nome)
        produtos = self.produto_repository.listar_todos_produtos()
        self.produto_view.mostrar_produtos(produtos)
