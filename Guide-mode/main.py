import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

c = 3.0 * 10**8
epsilon = 12.0  # 必要に応じてεの値を調整してください
w = 1  # wの値も調整する必要があるかもしれません

# k_yの方程式の左辺と右辺の差を計算する関数
def equation(ky, kx, w, epsilon):
    lhs = ky * np.tan(ky * w / 2)
    rhs = np.sqrt((1 - 1/epsilon) * kx**2 - ky**2 / epsilon)
    return lhs - rhs

# k_yの値を数値的に計算する関数
def compute_ky(kx_values, w, epsilon):
    ky_values = []
    kappa_values = []
    o_values = []
    for kx in kx_values:
        # fsolveを使用して方程式を数値的に解く
        ky_value = fsolve(equation, 0.000005, args=(kx, w, epsilon))
        print(ky_value)
        kappa = ky_value * np.tan(ky_value * w / 2)
        # kappa = np.sqrt((1 - 1/epsilon) * kx**2 - ky_value**2 / epsilon)
        kappa_values.append(kappa[0])
        o = c * np.sqrt(kx**2 - kappa**2)
        o_values.append(o[0])
    return [np.array(ky_values), np.array(kappa_values), np.array(o_values)]

kx = np.arange(0, 10, 0.01)
ky_values = compute_ky(kx, w, epsilon)[0]
kappa_values = compute_ky(kx, w, epsilon)[1]
o_values = compute_ky(kx, w, epsilon)[2]

plt.plot(kx * w / (2 * np.pi), o_values * w / (2 * np.pi * c))
plt.plot(kx * w / (2 * np.pi), kx * w / (2 * np.pi))
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('$k_x a / 2 \pi$')
plt.ylabel('$\omega w / 2 \pi c$')
plt.title('Dispersion Relation')
plt.grid(True)
plt.show()
