from planeta import Planeta

condicion_inicial = [10., 0., 0., 0.2]

mercurio = Planeta(condicion_inicial)

"""
Complete el código a continuación.
"""

mercurio_rk = Planeta(condicion_inicial)
mercurio_verlet = Planeta(condicion_inicial)
mercurio_beeman = Planeta(condicion_inicial)


# se simula la rotacion con runge kutta
i = 0
x_rk = []
y_rk = []
t_rk = []
E_rk = []
dt = 0.05

while i < 10:
    sol = mercurio_rk.y_actual
    x_rk.append(sol[0])
    y_rk.append(sol[1])
    t_rk.append(mercurio_rk.t_actual)
    E_rk.append(mercurio_rk.energia_total())
    mercurio_rk.avanza_rk4(dt)
    sol2 = mercurio_rk.y_actual
    if (sol[0] <= condicion_inicial[0] and condicion_inicial[0] < sol2[0])
    or (sol[0] >= condicion_inicial[0] and condicion_inicial[0] > sol2[0]):
        i += 1


# se simula la rotacion con verlet
i = 0
x_vv = []
y_vv = []
t_vv = []
E_vv = []
dt = 0.05

while i < 10:
    sol = mercurio_verlet.y_actual
    x_vv.append(sol[0])
    y_vv.append(sol[1])
    t_vv.append(mercurio_verlet.t_actual)
    E_vv.append(mercurio_verlet.energia_total())
    mercurio_verlet.avanza_verlet(dt)
    sol2 = mercurio_verlet.y_actual
    if (sol[0] <= condicion_inicial[0] and condicion_inicial[0] < sol2[0])
    or (sol[0] >= condicion_inicial[0] and condicion_inicial[0] > sol2[0]):
        i += 1


# se simula la rotacion con beeman
i = 0
x_bm = []
y_bm = []
t_bm = []
E_bm = []
dt = 0.05

while i < 10:
    sol = mercurio_beeman.y_actual
    x_bm.append(sol[0])
    y_bm.append(sol[1])
    t_bm.append(mercurio_beeman.t_actual)
    E_bm.append(mercurio_beeman.energia_total())
    mercurio_beeman.avanza_beeman(dt)
    sol2 = mercurio_beeman.y_actual
    if (sol[0] <= condicion_inicial[0] and condicion_inicial[0] < sol2[0])
    or (sol[0] >= condicion_inicial[0] and condicion_inicial[0] > sol2[0]):
        i += 1

