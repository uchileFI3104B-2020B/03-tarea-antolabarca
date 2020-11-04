import numpy as np

class Planeta(object):
    """
    Complete el docstring.
    """

    def __init__(self, condicion_inicial, alpha=0):
        """
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        """
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self):
        """
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        """
        x, y, vx, vy = self.y_actual
        r = np.sqrt(x**2 + y**2)
        aux = - r**(-3) + 2*self.alpha*r**(-4)
        fx = x * aux
        fy = y * aux
        return [vx, vy, fx, fy]

    def avanza_rk4(self, dt):
        """
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de RK4. El método no
        retorna nada, pero modifica los valores de self.y_actual y de
        self.t_actual.
        """
        pass

    def avanza_verlet(self, dt):
        """
        Similar a avanza_rk4, pero usando Verlet.
        """
        pass

    def avanza_beeman(self, dt):
        """
        Similar a avanza_rk4, pero usando Beeman.
        """
        pass

    def energia_total(self):
        """
        Calcula la enérgía total del sistema en las condiciones actuales.
        """
        pass


