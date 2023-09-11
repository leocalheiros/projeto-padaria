from src.controllers.produto_controller import ProdutoController
from src.views.produto_view import ProdutoView


def cadastrar_produto_process(nome: str, sabor: str, loja: str):
    cadastrar_produto_view = ProdutoView()
    cadastrar_produto_controller = ProdutoController()

    cadastrar_produto_controller.cadastrar_produto(nome, sabor, loja)
    cadastrar_produto_view.cadastrar_produto(nome, sabor, loja)
