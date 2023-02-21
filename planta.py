import math
from car import Car
from InvertedPendulum import InvertedPendulum
import sys
import constantes



class Planta:

    def __init__(self, coche, pendulo):
        self.coche = coche
        self.pendulo = pendulo
        self.posicion_anterior_pendulo_x = self.pendulo.devuelve_coordenada_x()
        self.velocidad_anterior_pendulo_x = self.pendulo.devuelve_velocidad_lineal_x()
        self.posicion_anterior_pendulo_y = self.pendulo.devuelve_coordenada_y()
        self.velocidad_anterior_pendulo_y = self.pendulo.devuelve_velocidad_lineal_y()
    def calcula_aceleracion_angular (self):
        aceleracion_lineal = self.pendulo.devuelve_aceleracion_lineal_x()
        aceleracion_angular = (1 / (self.pendulo.longitud_brazo_pendulo)) * ((constantes.GRAVEDAD * math.sin(self.pendulo.theta_actual)) - (aceleracion_lineal * math.cos(self.pendulo.theta_actual)))
        self.pendulo.actualizar_aceleracion_angular(aceleracion_angular)
        return aceleracion_angular
    def empujoncto_externo(self, aceleracion):
        aceleracion_nueva = self.pendulo.devuelve_aceleracion_angular() + aceleracion
        self.pendulo.actualizar_aceleracion_angular(aceleracion_nueva)
        return aceleracion_nueva
    def calcula_theta (self):
        theta = self.pendulo.theta_actual + (self.pendulo.devuelve_velocidad_angular() * constantes.delta_t) + ( 0.5 * self.pendulo.devuelve_aceleracion_angular() * constantes.delta_t * constantes.delta_t)
        self.pendulo.actualizar_coordenadas_pendulo(theta)
        return theta
    def calcula_omega (self):
        w = self.pendulo.velocidad_angular + (self.pendulo.devuelve_aceleracion_angular()*constantes.delta_t)
        self.pendulo.actualizar_omega (w)
        return w
    def calcula_aceleracion_lineal_x (self):
        aceleracion_x = (self.calcula_velocidad_lineal_x()-self.velocidad_anterior_pendulo_x) / constantes.delta_t
        self.pendulo.actualiza_aceleracion_lineal_x(aceleracion_x)
        self.velocidad_anterior_pendulo_x = self.pendulo.devuelve_velocidad_lineal_x()
        return aceleracion_x
    def calcula_velocidad_lineal_x (self):
        velocidad_x = 1/100 * ( self.pendulo.devuelve_coordenada_x() - self.posicion_anterior_pendulo_x) / constantes.delta_t
        #Divido entre 100 porque 100 pixels son 1metro
        self.posicion_anterior_pendulo_x = self.pendulo.devuelve_coordenada_x()
        self.pendulo.actualiza_velocidad_lineal_x(velocidad_x)
        return velocidad_x
    def calcula_fuerza_lineal_x_pendulo(self):
        fuerza_x = self.pendulo.masa_pendulo * self.calcula_aceleracion_lineal_x()
        return fuerza_x
#necesito tambien la componente y de todas estas magnitudes vectoriales
    def calcula_aceleracion_lineal_y (self):
        aceleracion_y = (self.calcula_velocidad_lineal_y()-self.velocidad_anterior_pendulo_y) / constantes.delta_t
        self.pendulo.actualiza_aceleracion_lineal_y(aceleracion_y)
        self.velocidad_anterior_pendulo_y = self.pendulo.devuelve_velocidad_lineal_y()
        return aceleracion_y
    def calcula_velocidad_lineal_y (self):
        velocidad_y = 1/100 * ( self.pendulo.devuelve_coordenada_y() - self.posicion_anterior_pendulo_y) / constantes.delta_t
        #Divido entre 100 porque 100 pixels son 1metro
        self.posicion_anterior_pendulo_y = self.pendulo.devuelve_coordenada_y()
        self.pendulo.actualiza_velocidad_lineal_y(velocidad_y)
        return velocidad_y
    def calcula_fuerza_lineal_y_pendulo(self):
        fuerza_y = self.pendulo.masa_pendulo * self.calcula_aceleracion_lineal_y()
        return fuerza_y