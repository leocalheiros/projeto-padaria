from typing import List
from src.controllers.produto_controller import ProdutoController
from src.views.produto_view import ProdutoView
from src.models.entities.produto import Produto


def listar_produtos_process():
    listar_produtos_view = ProdutoView()
    listar_produtos_controller = ProdutoController()

    produtos: List[Produto] = listar_produtos_controller.listar_todos_produtos()
    listar_produtos_view.mostrar_produtos(produtos)
