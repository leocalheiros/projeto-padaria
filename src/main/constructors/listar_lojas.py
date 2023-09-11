from typing import List
from src.controllers.loja_controller import LojaController
from src.views.loja_view import LojaView
from src.models.entities.loja import Loja


def listar_lojas_process():
    loja_controller = LojaController()
    loja_view = LojaView()

    lojas: List[Loja] = loja_controller.listar_todas_lojas()
    loja_view.mostrar_lojas(lojas)
