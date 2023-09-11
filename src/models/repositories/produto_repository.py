from typing import List
from src.models.entities.produto import Produto


class ProdutoRepository:
    def __init__(self) -> List:
        self.__produtos_list = []

    def cadastrar_produto(self, nome: str, sabor: str) -> None:
        produto = Produto(nome, sabor)
        self.__produtos_list.append(produto)

    def listar_produtos(self) -> List:
        return self.__produtos_list

    def deletar_produto(self, nome: str) -> None:
        self.__produtos_list.remove(self.__produtos_list.index(nome))
