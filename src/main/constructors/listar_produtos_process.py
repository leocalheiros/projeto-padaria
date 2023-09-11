from src.controllers.produto_controller import ProdutoController
from src.views.produto_view import ProdutoView


def listar_produtos_process(produto_controller: ProdutoController):
    listar_produtos_view = ProdutoView()

    produtos = produto_controller.listar_todos_produtos()
    listar_produtos_view.mostrar_produtos(produtos)
