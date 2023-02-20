'''
<Modelado y control del pendulo invertido>
    Copyright (C) <2023>  <Juan Jose Sorlí Castelló>
    sorli.castello@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-



# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import sys

import graficos
from car import Car
from Control import Control
from InvertedPendulum import InvertedPendulum
from planta import Planta
import constantes
import math

from graficos import Graficos

import tkinter as tk



# -----------
# Constantes
# -----------



# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------
def popupmsg(msg, title):
    root = tk.Tk()
    root.title(title)
    label = tk.Label(root, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    B1.pack()
    root.mainloop()


def main():
    coche_instanciado = Car(100)
    pendulo = InvertedPendulum(200,10,math.radians(0.5), coche_instanciado)
    coche_instanciado.desplazamiento(500)
    angulo = []
    aceleracion = []
    posicion = []
    contador_milisegundos = 0

    #pop up de licencia GPL v3
    texto_licencia = "Modelado y control del pendulo invertido Copyright 2023  Juan Jose Sorlí Castelló This program comes with ABSOLUTELY NO WARRANTY;This is free software under GPL v3 license, and you are welcome to redistribute it under certain conditions"
    popupmsg(texto_licencia, "Modelado y control del péndulo invertido Copyright")


    controlador = Control (coche_instanciado, pendulo)
    planta = Planta (coche_instanciado, pendulo)

    graficos_angulo = Graficos ("Angulo de inclinacion del péndulo","Tiempo","Theta")
    graficos_posicion = Graficos("Posición del carro","Tiempo","Posición")



    pygame.init()

    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((1200,800),0,32)

    posicion_coche = coche_instanciado.devuelve_posicion()



    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)



    screen.fill(BLACK)


    pygame.draw.rect(screen,WHITE,(posicion_coche,700,100,50))

    
    # se muestran lo cambios en pantalla
    pygame.display.flip()



    while True:
        # Posibles entradas del teclado y mouse
        empujoncito = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                graficos_angulo.pintar(angulo)
                graficos_posicion.pintar(posicion)
                graficos_angulo.salida()
                graficos_posicion.salida()

                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    empujoncito = 0.1
                elif event.button == 3:
                    empujoncito = -0.1

        pygame.display.update()


        screen.fill(BLACK)



        pygame.draw.rect(screen, WHITE, (coche_instanciado.devuelve_posicion(), 700, constantes.CAR_LENGTH, 50))
        pygame.draw.circle(screen, WHITE, (pendulo.devuelve_coordenada_x(), pendulo.devuelve_coordenada_y()), 15)
        pygame.draw.line(screen,BLUE,((coche_instanciado.devuelve_posicion()+(constantes.CAR_LENGTH/2)),700), (pendulo.devuelve_coordenada_x(), pendulo.devuelve_coordenada_y()), 4)


        controlador.control_coche_angulo()
        #controlador.control_coche_posicion(0)

        planta.calcula_aceleracion_lineal_x()
        planta.calcula_aceleracion_lineal_y()
        planta.calcula_aceleracion_angular()
        planta.empujoncto_externo(empujoncito)
        planta.calcula_omega()


        pendulo.actualizar_coordenadas_pendulo(planta.calcula_theta())

        posicion_coche = coche_instanciado.devuelve_posicion()


        print(pendulo.devuelve_theta())
        print(coche_instanciado.devuelve_posicion())
        

        angulo.append(pendulo.devuelve_theta())
        posicion.append(posicion_coche)



    #graficos.pintar(angulo)







if __name__ == "__main__":
    main()