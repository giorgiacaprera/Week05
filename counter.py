import flet as ft
from flet.core import page, row


def main(page : ft.Page):
    page.window.width = 400
    page.window.height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Counter"
    page.window_resizable = True

    # ICON BROWSER https://gallery.flet.dev/icons-browser/
    textOut = ft.TextField(width=100, text_size=24,
                           disabled = True, border_color="green",
                           text_align=ft.TextAlign.CENTER)

    textOut.value = 0

    def handlerMinus(e):
        currentVal = textOut.value
        if(currentVal > 0):
            currentVal = currentVal - 1
            textOut.value = currentVal
            textOut.update()

    def handlerPlus(e):
        currentVal = textOut.value
        currentVal = currentVal + 1
        textOut.value = currentVal
        textOut.update()


    btnMinus = ft.IconButton(icon = ft.Icons.REMOVE_CIRCLE_ROUNDED,
                             icon_size = 24, icon_color = "green",
                             on_click=handlerMinus)
    btnPlus = ft.IconButton(icon = ft.Icons.ADD_CIRCLE_ROUNDED,
                            icon_size = 24, icon_color = "green",
                            on_click=handlerPlus)

    row = ft.Row([btnMinus, textOut, btnPlus],
                 alignment=ft.MainAxisAlignment.CENTER)

    page.add(row)
    page.update()

ft.app(target=main)
