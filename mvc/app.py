import flet as ft
from model import Model
from controller import Controller
from view import View

def main(page : ft.Page):
    m = Model()
    #print(m.currentVal)
    v = View(page)
    #v.inizializzaGUI()
    c = Controller(v, m);
    v.impostaController(c) # In modo che nella View si possa avere accesso agli Handler
    v.inizializzaGUI() # Dopo aver impostato il controller
    v.aggiornaTextValue(0)

ft.app(target=main)