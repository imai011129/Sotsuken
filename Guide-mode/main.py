import sympy as sym
import math

# 定数定義
a = 1.0
w = 0.8 * a
c = 3.0 * 10**8
epsilon = 12.0
k_x = 1.0

x = sym.Symbol('x')
f = x * sym.tan(x * w / 2) 
g = sym.sqrt((1 - 1 / epsilon) * k_x - x**2 / epsilon)
solutions = sym.solve(f - g, x)

print(solutions)