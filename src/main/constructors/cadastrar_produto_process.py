from src.controllers.produto_controller import ProdutoController


def cadastrar_produto_process(nome: str, sabor: str, produto_controller: ProdutoController):
    produto_controller.cadastrar_produto(nome, sabor)
