from typing import List
from src.models.entities.loja import Loja


class LojaRepository:
    def __init__(self) -> List:
        self.__lojas_list = []

    def cadastrar_loja(self, nome: str) -> None:
        loja = Loja(nome)
        self.__lojas_list.append(loja)

    def listar_lojas(self) -> List[Loja]:
        return self.__lojas_list

    def deletar_loja(self, nome: str) -> None:
        if nome not in self.__lojas_list:
            print(f'Loja {nome} não encontrada!')
        for loja in self.__lojas_list:
            if loja.nome == nome:
                self.__lojas_list.remove(loja)
