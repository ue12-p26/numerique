import numpy as np
import matplotlib.pyplot as plt
import shutil
import os

if os.path.exists("Images"):
    shutil.rmtree("Images")  
os.makedirs("Images", exist_ok=True) 

x_min, x_max = -10., 10.
y_min, y_max = -10., 10.
mass_max = 3.
N = 3
Delta_t = 0.1
nb_incr = 500
G = 1.e1
eps = 1.e0
v_max = 1.
masses = np.random.uniform(0, mass_max, size=N)
X = np.random.uniform(x_min, x_max, N)
Y = np.random.uniform(y_min, y_max, N)
Vx = np.random.uniform(-v_max, v_max, N)
Vy = np.random.uniform(-v_max, v_max, N)

def acceleration(r):
    X = r[:, 0]
    Y = r[:, 1]

    Xi_Xj = X - X.reshape(-1, 1)
    Yi_Yj = Y - Y.reshape(-1, 1)
    norm = np.sqrt(Xi_Xj**2. + Yi_Yj**2. + eps)
    np.fill_diagonal(norm, np.inf)
    Dx_ij = Xi_Xj/norm**3.
    Dy_ij = Yi_Yj/norm**3.
    
    fx = G*Dx_ij.dot(masses)
    fy = G*Dy_ij.dot(masses)

    a = np.empty_like(r)
    a[:, 0] = fx
    a[:, 1] = fy

    return a

r_t = np.empty((N, 2, nb_incr)) # Stockage des solutions à chaque incrément
v_t = np.empty((N, 2, nb_incr))

r = np.empty((N, 2)) # X, Y
r[:, 0] = X
r[:, 1] = Y

v = np.empty((N, 2)) # Vx, Vy
v[:, 0] = Vx
v[:, 1] = Vy

r_t[:, :, 0] = r
v_t[:, :, 0] = v

E_cin_t = np.empty((nb_incr))

for incr in range(1, nb_incr) :
    a_i = acceleration(r)
    v_ip05 = v + 0.5*Delta_t*a_i
    r += Delta_t*v_ip05
    a_ip1 = acceleration(r)
    v = v_ip05 + 0.5*Delta_t*a_ip1

    vx = v[:, 0]
    vy = v[:, 1]
    E_cin = 0.5*masses.dot(vx**2. + vy**2.)

    r_t[:, :, incr] = r
    v_t[:, :, incr] = v
    E_cin_t[incr] = E_cin

# Visualisation 
scale = 3.
colors = np.random.uniform(0.3, 1., size=(N, 3))

fig, ax = plt.subplots()

for incr in range(nb_incr):
    ax.scatter(r_t[:, 0, incr], r_t[:, 1, incr], color=colors)

    for i in range(N):
        ax.plot(r_t[i, 0, :incr], r_t[i, 1, :incr], color=colors[i], lw=1.5)
    
    ax.set_xlim(scale*x_min, scale*x_max)
    ax.set_ylim(scale*y_min, scale*y_max)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.style.use('dark_background')

    fig.savefig(f"Images/{incr}.png")
    ax.clear()

plt.close()
plt.plot(range(nb_incr), E_cin_t)
plt.savefig("Images/energy.png")