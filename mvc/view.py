import flet as ft
from controller import Controller

class View():
    def __init__(self, page : ft.Page):
        self._page = page
        self._controller = None

    def impostaController(self, controller):
        self._controller = controller

    def inizializzaGUI(self):
        self._page.window.width = 400
        self._page.window.height = 300
        self._page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self._page.title = "Counter"
        self._page.window_resizable = True

        self._textOut = ft.TextField(width=100, text_size=24,
                                     disabled=True, border_color="green",
                                     text_align=ft.TextAlign.CENTER)

        btnMinus = ft.IconButton(icon = ft.Icons.REMOVE_CIRCLE_ROUNDED,
                                 icon_size = 24, icon_color = "green",
                                 on_click=self._controller.handlerMinus) # Utilizzo dellHandler in controller

        btnPlus = ft.IconButton(icon = ft.Icons.ADD_CIRCLE_ROUNDED,
                                icon_size = 24, icon_color = "green",
                                on_click=self._controller.handlerPlus)

        row = ft.Row([btnMinus, self._textOut, btnPlus],
                     alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row)
        self._page.update()

    def aggiornaTextValue(self, value):
        self._textOut.value = value
        self._page.update();