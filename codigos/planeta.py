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
        return np.array([vx, vy, fx, fy])


    # los siguientes métodos corresponden al cálculo de Runge Kutta de Orden 4
    def K1(self, dt):
        """
        Calcula la cte K1 del algoritmo de Runge-Kutta
        """
        return dt * self.ecuacion_de_movimiento()

    def K2(self, dt):
        """
        Calcula la cte K2 del algoritmo de Runge-Kutta
        """
        return dt * self.ecuacion_de_movimiento()

    def K3(self, dt):
        """
        Calcula la cte K3 del algoritmo de Runge-Kutta
        """
        return dt * self.ecuacion_de_movimiento()

    def K4(self, dt):
        """
        Calcula la cte K4 del algoritmo de Runge-Kutta
        """
        return dt * self.ecuacion_de_movimiento()

    def avanza_rk4(self, dt):
        """
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de RK4. El método no
        retorna nada, pero modifica los valores de self.y_actual y de
        self.t_actual.
        """
        k1_n = self.K1(dt)
        self.t_actual += dt/2
        self.y_actual += k1_n/2
        k2_n = self.K2(dt)
        self.y_actual -= k1_n/2
        self.y_actual += k2_n/2
        k3_n = self.K3(dt)
        self.t_actual += dt/2
        self.y_actual += k3_n
        self.y_actual -= k2_n/2
        k4_n = self.K4(dt)
        ans = self.y_actual + (k1_n + 2*k2_n + 2*k3_n + k4_n)/6
        self.y_actual = ans


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


