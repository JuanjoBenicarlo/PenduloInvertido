import math
from car import Car
#https://upcommons.upc.edu/bitstream/handle/2117/188939/sec_pv1_pendulo_invertido_1314a-5195.pdf
import constantes



class InvertedPendulum:
    def __init__(self, brazo_pendulo, masa_pendulo, theta_inicial, coche):
        self.theta_inicial = theta_inicial
        self.theta_actual = theta_inicial
        self.longitud_brazo_pendulo = brazo_pendulo

        self.pos_x_inicial_pendulo = brazo_pendulo * math.sin(self.theta_inicial)
        self.pos_y_inicial_pendulo = brazo_pendulo * math.cos(self.theta_inicial)
        self.pos_x_actual_pendulo = self.pos_x_inicial_pendulo
        self.pos_y_actual_pendulo = self.pos_y_inicial_pendulo

        self.masa_pendulo = masa_pendulo
        self.coche_instanciado = coche

        self.velocidad_angular = 0
        self.aceleracion_angular = 0
        self.velocidad_lineal_x = 0
        self.aceleracion_lineal_x = 0
        self.velocidad_lineal_y = 0
        self.aceleracion_lineal_y = 0
    def actualizar_coordenadas_pendulo(self, theta_actual):
        self.theta_actual = theta_actual
        self.pos_x_actual_pendulo = self.coche_instanciado.devuelve_posicion() + (constantes.CAR_LENGTH / 2) + (self.longitud_brazo_pendulo * math.sin(self.theta_actual))
        self.pos_y_actual_pendulo = (700 - (self.longitud_brazo_pendulo * math.cos(self.theta_actual)))

    def devuelve_coordenada_x (self):
        return self.pos_x_actual_pendulo
    def devuelve_coordenada_y (self):
        return self.pos_y_actual_pendulo
    def actualizar_omega (self, w):
        self.velocidad_angular = w
    def actualizar_aceleracion_angular (self, alfa):
        self.aceleracion_angular = alfa
    def actualiza_aceleracion_lineal_x(self, accel):
        self.aceleracion_lineal_x = accel

    def actualiza_aceleracion_lineal_y(self, accel):
        self.aceleracion_lineal_y = accel
    def actualiza_velocidad_lineal_x(self, speed):
        self.velocidad_lineal_x = speed

    def actualiza_velocidad_lineal_y(self, speed):
        self.velocidad_lineal_y = speed

    def devuelve_aceleracion_angular(self):
        return self.aceleracion_angular
    def devuelve_velocidad_angular(self):
        return self.velocidad_angular
    def devuelve_velocidad_lineal_x(self):
        return self.velocidad_lineal_x
    def devuelve_aceleracion_lineal_x(self):
        return self.aceleracion_lineal_x
    def devuelve_velocidad_lineal_y(self):
        return self.velocidad_lineal_y
    def devuelve_aceleracion_lineal_y(self):
        return self.aceleracion_lineal_y
    def devuelve_theta(self):
        return self.theta_actual

    def devuelve_aceleracion_lineal(self):
        return math.sqrt(math.pow(self.aceleracion_lineal_x, 2)  + math.pow(self.aceleracion_lineal_y, 2))
