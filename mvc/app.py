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
    v.impostaController(c) # IN MODO CHE NELLA VIEW SI POSSA AVERE ACCESSO AGLI HANDLER
    v.inizializzaGUI() # DOPO AVER IMPOSTATO IL CONTROLLER
    v.aggiornaTextValue(0)


ft.app(target=main)