from planeta import Planeta
from matplotlib import pyplot as plt

condicion_inicial = [10., 0., 0., 0.2]
alpha = 10**(-2.551)

mercurio = Planeta(condicion_inicial)

"""
Complete el código a continuación.
"""

mercurio_rk = Planeta(condicion_inicial)
mercurio_verlet = Planeta(condicion_inicial)
mercurio_beeman = Planeta(condicion_inicial)


# se simula la rotacion con runge kutta
i = 0
j = 0
x_rk = []
y_rk = []
t_rk = []
E_rk = []
dt = 0.05

sol = mercurio_rk.y_actual
x_rk.append(sol[0])
y_rk.append(sol[1])
t_rk.append(mercurio_verlet.t_actual)
E_rk.append(mercurio_verlet.energia_total())

while i < 10:
    mercurio_rk.avanza_rk4(dt)
    sol = mercurio_rk.y_actual
    x_rk.append(sol[0])
    y_rk.append(sol[1])
    t_rk.append(mercurio_rk.t_actual)
    E_rk.append(mercurio_rk.energia_total())
    j += 1
    if (y_rk[j-1] <= 0 and 0 < y_rk[j]) or (y_rk[j-1] >= 0 and 0 > y_rk[j]):
        i += 1


# se simula la rotacion con verlet
i = 0
j = 0
x_vv = []
y_vv = []
t_vv = []
E_vv = []
dt = 0.05

sol = mercurio_verlet.y_actual
x_vv.append(sol[0])
y_vv.append(sol[1])
t_vv.append(mercurio_verlet.t_actual)
E_vv.append(mercurio_verlet.energia_total())

while i < 10:
    mercurio_verlet.avanza_verlet(dt)
    sol = mercurio_verlet.y_actual
    x_vv.append(sol[0])
    y_vv.append(sol[1])
    t_vv.append(mercurio_verlet.t_actual)
    E_vv.append(mercurio_verlet.energia_total())
    j += 1
    if (y_vv[j-1] <= 0 and 0 < y_vv[j]) or (y_vv[j-1] >= 0 and 0 > y_vv[j]):
        i += 1


# se simula la rotacion con beeman
i = 0
j = 0
x_bm = []
y_bm = []
t_bm = []
E_bm = []
dt = 0.05
sol = mercurio_beeman.y_actual
x_bm.append(sol[0])
y_bm.append(sol[1])
t_bm.append(mercurio_beeman.t_actual)
E_bm.append(mercurio_beeman.energia_total())


while i < 10:
    mercurio_beeman.avanza_beeman(dt)
    sol = mercurio_beeman.y_actual
    x_bm.append(sol[0])
    y_bm.append(sol[1])
    t_bm.append(mercurio_beeman.t_actual)
    E_bm.append(mercurio_beeman.energia_total())
    j += 1
    if (y_bm[j-1] <= 0 and 0 < y_bm[j]) or (y_bm[j-1] >= 0 and 0 > y_bm[j]):
        i += 1


# plot de energia con cada metodo
plt.figure(1)
plt.clf()
plt.plot(t_rk, E_rk, label="Energía total con Runge Kutta")
plt.plot(t_bm, E_bm, label="Energía total con Beeman")
plt.plot(t_vv, E_vv, label="Energía total con Velocity Verlet")
plt.xlabel("tiempo")
plt.ylabel("energía")
plt.legend()
plt.show()

# plot de la orbita con runge kutta
plt.figure(2)
plt.clf()
plt.plot(x_rk, y_rk)
plt.xlabel("posición del planeta en el eje X")
plt.ylabel("posición del planeta en el eje Y")
plt.show()

# plot de la orbita con velocity verlet
plt.figure(3)
plt.clf()
plt.plot(x_vv, y_vv)
plt.xlabel("posición del planeta en el eje X")
plt.ylabel("posición del planeta en el eje Y")
plt.show()

# plot de la orbita con beeman
plt.figure(4)
plt.clf()
plt.plot(x_bm, y_bm)
plt.xlabel("posición del planeta en el eje X")
plt.ylabel("posición del planete en el eje Y")
plt.show()


# se simula la rotacion con alpha mayor a 0
mercurio_alpha = Planeta(condicion_inicial, alpha)

i = 0
j = 0
x_a = []
y_a = []
t_a = []
E_a = []
dt = 0.05
sol = mercurio_alpha.y_actual
x_a.append(sol[0])
y_a.append(sol[1])
t_a.append(mercurio_alpha.t_actual)
E_a.append(mercurio_alpha.energia_total())

while i < 60:
    mercurio_alpha.avanza_beeman(dt)
    sol = mercurio_alpha.y_actual
    x_a.append(sol[0])
    y_a.append(sol[1])
    t_a.append(mercurio_alpha.t_actual)
    E_a.append(mercurio_alpha.energia_total())
    j += 1
    if (y_a[j-1] <= 0 and 0 < y_a[j]) or (y_a[j-1] >= 0 and 0 > y_a[j]):
        i += 1