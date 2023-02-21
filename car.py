


class Car:
    def __init__(self, masa_coche):
        self.posicion_x=0
        self.masa_coche = masa_coche
        self.velocidad = 0
        self.rozamiento = 0
    def desplazamiento(self, delta_x):
        self.posicion_x = delta_x
    def devuelve_posicion(self):
        return self.posicion_x
    def devuelve_velocidad(self):
        return self.velocidad
    def actualiza_velocidad(self, speed):
        self.velocidad = speed


