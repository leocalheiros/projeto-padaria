from src.controllers.produto_controller import ProdutoController
from src.views.produto_view import ProdutoView


def deletar_produto_process(produto):
    deletar_produto_view = ProdutoView()
    deletar_produto_controller = ProdutoController()

    deletar_produto_controller.deletar_produto(produto)
    deletar_produto_view.deletar_produto(produto)
