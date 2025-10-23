import flet as ft
from model import Model

class Controller():
    def __init__(self, view : ft.View, model : Model):
        self._view = view
        self._model= model

    def handlerMinus(self, e):
        self._model.currentVal -= 1
        #self._view.textOut.value
        #self._view.update()
        self._view.aggiornaTextValue(self._model.currentVal)

    def handlerPlus(self, e):
        self._model.currentVal += 1
        #self._view.textOut.value
        #self._view.update()
        self._view.aggiornaTextValue(self._model.currentVal)
