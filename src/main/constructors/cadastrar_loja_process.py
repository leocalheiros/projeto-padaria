from src.controllers.loja_controller import LojaController
from src.views.loja_view import LojaView


def cadastrar_loja_process(nome: str):
    cadastrar_loja_view = LojaView()
    cadastrar_loja_controller = LojaController()

    cadastrar_loja_controller.cadastrar_loja(nome)
    cadastrar_loja_view.cadastrar_loja(nome)
