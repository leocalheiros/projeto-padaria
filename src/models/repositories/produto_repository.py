from typing import List
from src.models.entities.produto import Produto


class ProdutoRepository:
    def __init__(self):
        self.__produtos_list = []

    def cadastrar_produto(self, nome: str, sabor: str):
        produto = Produto(nome, sabor)
        self.__produtos_list.append(produto)
        print("Produtos na lista:")
        for produto in self.__produtos_list:
            print(f"Nome: {produto.nome}, Sabor: {produto.sabor}")

    def listar_todos_produtos(self) -> List[Produto]:
        return self.__produtos_list

    def deletar_produto(self, nome: str):
        for produto in self.__produtos_list:
            if produto.nome == nome:
                self.__produtos_list.remove(produto)
                break
