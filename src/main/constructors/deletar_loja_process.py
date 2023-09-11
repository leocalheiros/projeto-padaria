from src.controllers.loja_controller import LojaController
from src.views.loja_view import LojaView


def deletar_loja_process(nome: str):
    deletar_loja_controller = LojaController()
    deletar_loja_view = LojaView()

    deletar_loja_controller.deletar_loja(nome)
    deletar_loja_view.deletar_loja(nome)
