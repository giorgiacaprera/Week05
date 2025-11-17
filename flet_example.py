from time import sleep
import flet as ft

def main(page : ft.Page):
    myText = ft.Text(value = "Hello world!",
                     size = 50,
                     color = "red")
    # Aggiungo il controllo alla pagina
    page.controls.append( myText )
    # Aggiorno la pagine
    page.update()

    myText.color = "blue"
    sleep(5) # Pausa di 5 secondi
    myText.update()

    # Definisco la funzione EVENT HANDLER del CLICK sul pulsante btnPress
    def btnPressHandler(e):
        print("Button pressed")
        myText.color = "green"
        myText.update()

    btnPress = ft.ElevatedButton(text="Premi qui!", on_click=btnPressHandler)
    page.controls.append(btnPress)
    page.update()


ft.app(target=main, view = ft.AppView.FLET_APP)