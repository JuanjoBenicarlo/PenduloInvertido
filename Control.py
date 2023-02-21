
import sys
from car import Car
from InvertedPendulum import InvertedPendulum
import math
import constantes


class Control:

    def __init__(self, coche, pendulo):
        self.coche = coche
        self.pendulo = pendulo
        self.error_angulo_anterior = 0
        self.error_angulo_acumulado = 0
        self.error_posicion_anterior = 0
        self.error_posicion_acumulado = 0


    def control_coche_angulo(self):

        error_angulo= 0
        derivada_error_angulo=0


        aceleracion = 0   
        if (self.pendulo.devuelve_theta()>=0 and self.pendulo.devuelve_theta()<0.5):
            error_angulo =  abs(self.pendulo.devuelve_theta()) - 0
            derivada_error_angulo = (error_angulo - self.error_angulo_anterior) / constantes.delta_t
            self.error_angulo_anterior = error_angulo
            self.error_angulo_acumulado += error_angulo
            aceleracion = (800.25 * error_angulo) + (87.9 * derivada_error_angulo) + (0.3 * self.error_angulo_acumulado)

        if(self.pendulo.devuelve_theta()>=0 and self.pendulo.devuelve_theta()>5.78):
            error_angulo = abs(self.pendulo.devuelve_theta())-6.28
            derivada_error_angulo = ( self.error_angulo_anterior - error_angulo ) / constantes.delta_t
            self.error_angulo_anterior = error_angulo
            self.error_angulo_acumulado += error_angulo
            aceleracion = ((800.25 * error_angulo) + (87.9 * derivada_error_angulo) + (0.3 * self.error_angulo_acumulado))

        if (self.pendulo.devuelve_theta()<0 and self.pendulo.devuelve_theta()>-0.5):
            error_angulo =  self.pendulo.devuelve_theta() - 0
            derivada_error_angulo = (error_angulo - self.error_angulo_anterior) / constantes.delta_t
            self.error_angulo_anterior = error_angulo
            self.error_angulo_acumulado += error_angulo
            aceleracion = (800.25 * error_angulo) + (87.9 * derivada_error_angulo) + (0.3 * self.error_angulo_acumulado)

        if(self.pendulo.devuelve_theta()<0 and self.pendulo.devuelve_theta()<-5.78):
            error_angulo = self.pendulo.devuelve_theta()-6.28
            derivada_error_angulo = ( self.error_angulo_anterior - error_angulo ) / constantes.delta_t
            self.error_angulo_anterior = error_angulo
            self.error_angulo_acumulado += error_angulo
            aceleracion = ((800.25 * error_angulo) + (87.9 * derivada_error_angulo) + (0.3 * self.error_angulo_acumulado))

        self.control_coche_posicion(aceleracion)

    def control_coche_posicion(self, aceleracion):

        error_posicion = 0
        derivada_error_posicion = 0

        aceleracion_final = 0
        error_posicion = self.coche.devuelve_posicion() - 650


        derivada_error_posicion = (error_posicion - self.error_posicion_anterior) / constantes.delta_t
        self.error_posicion_anterior = error_posicion
        self.error_posicion_acumulado += error_posicion
        aceleracion_final = (1000 * aceleracion) + (1.7 * error_posicion) + (2.7 * derivada_error_posicion) + (0.0003 * self.error_posicion_acumulado)


        self.aplica_aceleracion(aceleracion_final)



    def aplica_aceleracion(self, aceleracion):

        velocidad = self.coche.devuelve_velocidad() + (aceleracion * constantes.delta_t)

        self.coche.actualiza_velocidad(velocidad)

        xf = self.coche.devuelve_posicion() + (velocidad * constantes.delta_t) + (0.5 * aceleracion * constantes.delta_t * constantes.delta_t)

        self.coche.desplazamiento(xf)


