import flet as ft
from flet import Row
from flet import Checkbox
from flet import ListView

def main(page : ft.Page):
    page.window.width = 400
    page.window.height = 700
    page.title = "Todolist"
    page.update()

    listItems = []

    textIn = ft.TextField(label="Item to add")

    # CREO UN CONTENITORE DOTATO DI BARRA DI SCORRIMENTO
    lv = ListView(expand=True)

    def btnAdd(e):
        value = textIn.value # LEGGO QUANTO INSERITO DALL'UTENTE
        tempCheckbox = Checkbox(label=value)
        #page.controls.append(tempCheckbox)
        # ANZICHE' AGGIUNGERE ALLA page POSSO AGGIUNGERE AD UNA ListView
        lv.controls.append(Row([tempCheckbox], ft.MainAxisAlignment.START))
        page.update()

    btnAdd = ft.CupertinoButton(text="Add", on_click=btnAdd)

    #page.controls.append(textIn)
    #page.controls.append(btnAdd)

    # ORGANIZZO I MIEI CONTROLLI SU UNA RIGA
    row1 = Row([textIn, btnAdd], alignment=ft.MainAxisAlignment.CENTER)
    page.controls.append(row1)
    #page.add(row1) # EQUIVALENTE A controls.append()

    page.controls.append(lv) #page.add(lv)




    page.update()


ft.app(target=main)