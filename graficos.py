import numpy as np
import time
import matplotlib.pyplot as plt
import constantes

class Graficos:

    def __init__(self, titulo, labelX, labelY):

        plt.ion()

        self.figure, self.ax = plt.subplots(figsize=(8, 6))

        plt.title(titulo, fontsize=25)

        plt.xlabel(labelX, fontsize=18)
        plt.ylabel(labelY, fontsize=18)


    def pintar (self, variable_ordenadas):

        variable_independiente = np.linspace(0,len(variable_ordenadas)*constantes.delta_t,len(variable_ordenadas))


        line1 = self.ax.plot(variable_independiente, variable_ordenadas)

        self.figure.canvas.draw()

        self.figure.canvas.flush_events()


    def salida(self):
        plt.show(block = True)

