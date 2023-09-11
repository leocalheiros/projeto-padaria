from src.controllers.produto_controller import ProdutoController


def deletar_produto_process(produto, produto_controller: ProdutoController):
    produto_controller.deletar_produto(produto)
