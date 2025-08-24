# calculus_sympy.py
import sympy as sp

# Define variables
x, y, n = sp.symbols('x y n')
f = sp.Function('f')

# 1. Derivatives
expr1 = sp.sin(x)*sp.exp(x)
deriv1 = sp.diff(expr1, x)
print("Derivative of sin(x)*e^x:", deriv1)

# Higher-order derivative
deriv2 = sp.diff(sp.cos(x), x, 2)
print("Second derivative of cos(x):", deriv2)

# Partial derivatives
expr2 = x*2 * y*3
partial_x = sp.diff(expr2, x)
partial_y = sp.diff(expr2, y)
print("∂/∂x of x^2*y^3:", partial_x)
print("∂/∂y of x^2*y^3:", partial_y)

# 2. Integrals
# Indefinite integral
integral1 = sp.integrate(sp.sin(x)*sp.exp(x), x)
print("∫ sin(x)e^x dx:", integral1)

# Definite integral
integral2 = sp.integrate(x**2, (x, 0, 3))
print("∫₀³ x^2 dx:", integral2)

# Improper integral
integral3 = sp.integrate(1/(x**2 + 1), (x, -sp.oo, sp.oo))
print("∫ -∞ to ∞ of 1/(x²+1):", integral3)

# 3. Limits
limit1 = sp.limit(sp.sin(x)/x, x, 0)
print("lim x→0 sin(x)/x:", limit1)

limit2 = sp.limit((1 + 1/n)**n, n, sp.oo)
print("lim n→∞ (1 + 1/n)^n:", limit2)

# 4. Series Expansion
series1 = sp.series(sp.sin(x), x, 0, 6)
print("Taylor series of sin(x) around 0 to 5 terms:", series1)

series2 = sp.series(sp.ln(1 + x), x, 0, 5)
print("Taylor series of ln(1+x) around 0 to 4 terms:", series2)

# 5. Multivariable Calculus
grad = [sp.diff(expr2, var) for var in (x, y)]
print("Gradient of x²y³:", grad)

# 6. Evaluate a derivative/integral at a point
val = sp.diff(sp.exp(x)*sp.sin(x), x).subs(x, sp.pi)
print("d/dx [e^x*sin(x)] at x = π:", val)

int_val = sp.integrate(x**2, (x, 0, 1)).evalf()
print("Numerical value of ∫₀¹ x² dx:", int_val)