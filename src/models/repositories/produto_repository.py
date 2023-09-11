from typing import List
from src.models.entities.produto import Produto


class ProdutoRepository:
    def __init__(self) -> List:
        self.__produtos_list = []

    def cadastrar_produto(self, nome: str, sabor: str, loja: str) -> None:
        produto = Produto(nome, sabor, loja)
        self.__produtos_list.append(produto)

    def listar_todos_produtos(self) -> List:
        return self.__produtos_list

    def deletar_produto(self, nome: str) -> None:
        for produto in self.__produtos_list:
            if produto.nome == nome:
                self.__produtos_list.remove(produto)
                break
