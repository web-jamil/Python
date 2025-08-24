# equation_solving_sympy.py
import sympy as sp

# Define symbols
x, y, z = sp.symbols('x y z')

# 1. Linear equation in one variable
eq1 = sp.Eq(2*x - 4, 0)
sol1 = sp.solve(eq1, x)
print("Linear equation:", eq1)
print("Solution:", sol1)

# 2. Quadratic equation
eq2 = sp.Eq(x**2 - 5*x + 6, 0)
sol2 = sp.solve(eq2, x)
print("\nQuadratic equation:", eq2)
print("Solutions:", sol2)

# 3. Cubic/Polynomial equation
eq3 = sp.Eq(x*3 - 6*x*2 + 11*x - 6, 0)
sol3 = sp.solve(eq3, x)
print("\nCubic equation:", eq3)
print("Solutions:", sol3)

# 4. System of linear equations
eq4 = sp.Eq(2*x + y, 5)
eq5 = sp.Eq(3*x - y, 4)
sol_sys = sp.solve((eq4, eq5), (x, y))
print("\nSystem of linear equations:")
print(eq4)
print(eq5)
print("Solution:", sol_sys)

# 5. System of nonlinear equations
eq6 = sp.Eq(x*2 + y*2, 25)
eq7 = sp.Eq(x - y, 1)
sol_nonlin = sp.solve((eq6, eq7), (x, y))
print("\nSystem of nonlinear equations:")
print(eq6)
print(eq7)
print("Solutions:", sol_nonlin)

# 6. Inequality solving
ineq1 = sp.solve_univariate_inequality(x**2 - 4 > 0, x)
print("\nInequality x^2 - 4 > 0:")
print("Solution:", ineq1)

# 7. Solve with parameters
a, b = sp.symbols('a b')
eq_param = sp.Eq(a*x + b, 0)
sol_param = sp.solve(eq_param, x)
print("\nEquation with parameters:", eq_param)
print("Solution:", sol_param)

# 8. Piecewise-defined solution
eq_piece = sp.Eq(sp.Abs(x - 3), 5)
sol_piece = sp.solve(eq_piece, x)
print("\nEquation with absolute value:", eq_piece)
print("Solutions:", sol_piece)

# 9. Transcendental equations (numeric solution)
eq_trans = sp.Eq(sp.exp(x) - x**2, 0)
sol_trans = sp.nsolve(eq_trans, x, 1.0)
print("\nTranscendental equation (e^x = x^2):")
print("Approximate solution near x=1:", sol_trans)

# 10. Differential equation (simple first-order)
f = sp.Function('f')
diff_eq = sp.Eq(f(x).diff(x), f(x))
sol_diff = sp.dsolve(diff_eq, f(x))
print("\nDifferential equation f'(x) = f(x):")
print("Solution:", sol_diff)