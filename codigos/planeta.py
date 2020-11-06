import numpy as np

class Planeta(object):
    """
    La clase Planeta representa planetas. 

    Un planeta posee los siguientes valores asociados:
        y_actual (np.array) las condiciones actuales de posicion y velocidad
        t_actual (float) el tiempo actual
        alpha (float) el valor de alpha

    Ademas se tienen metodos para avanzar "un paso" (resolviendo la EDO
    asociada) con 3 metodos numericos distintos: runge-kutta de orden 4,
    beeman y verlet

    """

    def __init__(self, condicion_inicial, alpha=0):
        """
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Recibe una condicion inicial (un vector de 4 valores) y opcionalmente
        el valor de alpha (si no se ingresa, el default es 0)

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


    def avanza_rk4(self, dt):
        """
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de RK4. El método no
        retorna nada, pero modifica los valores de self.y_actual y de
        self.t_actual.
        """
        k1_n = dt * self.ecuacion_de_movimiento()
        self.t_actual += dt/2
        self.y_actual += k1_n/2
        k2_n = dt * self.ecuacion_de_movimiento()
        self.y_actual -= k1_n/2
        self.y_actual += k2_n/2
        k3_n = dt * self.ecuacion_de_movimiento()
        self.t_actual += dt/2
        self.y_actual += k3_n
        self.y_actual -= k2_n/2
        k4_n = dt * self.ecuacion_de_movimiento()
        ans = self.y_actual + (k1_n + 2*k2_n + 2*k3_n + k4_n)/6
        self.y_actual = ans


    def avanza_verlet(self, dt):
        """
        Similar a avanza_rk4, pero usando Verlet (Velocity Verlet)
        """
        x, y, vx, vy = self.y_actual
        x_n = np.array([x, y])
        v_n = np.array([vx, vy])
        mov = self.ecuacion_de_movimiento()
        a_n = np.array([mov[2], mov[3]])
        x_n1 = x_n + v_n*dt + a_n*dt*dt/2
        self.y_actual[0] = x_n1[0]
        self.y_actual[1] = x_n1[1]
        mov1 = self.ecuacion_de_movimiento()
        a_n1 = np.array([mov1[2], mov1[3]])
        v_n1 = v_n + (a_n + a_n1)*dt/2
        self.y_actual[2] = v_n1[0]
        self.y_actual[3] = v_n1[1]
        self.t_actual += dt


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

mercurio = Planeta([1,1,2,3])
print(mercurio.y_actual)
mercurio.avanza_verlet(0.1)
print(mercurio.y_actual)
print(mercurio.t_actual)