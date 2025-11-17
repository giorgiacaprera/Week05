import flet as ft
from flet import Row
from flet import Checkbox
from flet import ListView

def main(page : ft.Page):
    page.window.width = 400
    page.window.height = 700
    page.title = "Todolist"
    page.update()

    textIn = ft.TextField(label="Item to add")

    # Creo un contenitore dotato di una BARRA DI SCORRIMENTO
    lv = ListView(expand=True)

    def btnAdd(e):
        value = textIn.value # Leggo quanto inserito dall'utente
        tempCheckbox = Checkbox(label=value)
        # Aggiungo temoCheckbox alla ListView
        lv.controls.append(Row([tempCheckbox], ft.MainAxisAlignment.START))
        page.update()

    btnAdd = ft.CupertinoButton(text="Add", on_click=btnAdd)

    #page.controls.append(textIn)
    #page.controls.append(btnAdd)

    # Organizzo i miei controlli su una riga
    row1 = Row([textIn, btnAdd], alignment=ft.MainAxisAlignment.CENTER)
    page.controls.append(row1)
    #page.add(row1) # EQUIVALENTE A controls.append()
    page.controls.append(lv) # EQUIVALENTE A page.add(lv)
    page.update()


ft.app(target=main)