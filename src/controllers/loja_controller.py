from src.models.repositories.loja_repository import LojaRepository
from src.views.loja_view import LojaView


class LojaController:
    def __init__(self):
        self.loja_repository = LojaRepository()
        self.loja_view = LojaView()

    def cadastrar_loja(self, nome: str) -> None:
        self.loja_repository.cadastrar_loja(nome)
        self.loja_view.cadastrar_loja(nome)

    def listar_todas_lojas(self) -> any:
        lojas = self.loja_repository.listar_lojas()
        self.loja_view.mostrar_lojas(lojas)

    def deletar_loja(self, nome: str) -> None:
        self.loja_repository.deletar_loja(nome)
        self.loja_view.deletar_loja(nome)
        lojas = self.loja_repository.listar_lojas()
        self.loja_view.mostrar_lojas(lojas)
