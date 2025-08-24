# symbolic_algebra_sympy.py
import sympy as sp

# Define symbols
x, y, z, a, b = sp.symbols('x y z a b')
f = sp.Function('f')

# 1. Expression creation
expr1 = (x + y)**2
print("Expression:", expr1)

# 2. Expansion
expanded = sp.expand(expr1)
print("Expanded:", expanded)

# 3. Factoring
factored = sp.factor(expanded)
print("Factored:", factored)

# 4. Simplification
expr2 = sp.sin(x)*2 + sp.cos(x)*2
simplified = sp.simplify(expr2)
print("Simplified sin²x + cos²x:", simplified)

# More simplification
expr3 = (x**2 - 1)/(x - 1)
simplified2 = sp.simplify(expr3)
print("Simplified (x² - 1)/(x - 1):", simplified2)

# 5. Substitution
expr4 = x*2 + y*2
subbed = expr4.subs({x: 3, y: 4})
print("Substitution x=3, y=4 in x² + y²:", subbed)

# 6. Symbolic equations
eq = sp.Eq(x**2 - 4, 0)
solutions = sp.solve(eq, x)
print("Solving equation x² - 4 = 0:", solutions)

# 7. Rational simplification
rat_expr = (x**2 - 9)/(x + 3)
rat_simplified = sp.cancel(rat_expr)
print("Simplified rational expression:", rat_simplified)

# 8. Collect like terms
expr5 = x*y + x*z + x*a
collected = sp.collect(expr5, x)
print("Collected terms by x:", collected)

# 9. Symbolic functions
f_expr = f(x) + 2*f(x)
simplified_func = sp.simplify(f_expr)
print("Simplified symbolic function expression:", simplified_func)

# 10. Substituting symbolic functions
f_def = x**2 + 1
replaced_f = f_expr.subs(f(x), f_def)
print("Replaced f(x) with x²+1:", replaced_f)

# 11. Polynomial tools
poly = sp.poly(x*3 + 3*x*2 + 3*x + 1)
print("Degree of polynomial:", poly.degree())
print("Coefficients:", poly.all_coeffs())
print("Roots:", poly.all_roots())

# 12. Expression comparison
expr6 = sp.expand((x + 1)**2)
expr7 = x**2 + 2*x + 1
are_equal = sp.simplify(expr6 - expr7) == 0
print("Are expressions equal?", are_equal)