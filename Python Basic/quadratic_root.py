import math
import cmath  # For complex roots

def quadratic_roots(a, b, c):
    """Calculate the roots of a quadratic equation ax² + bx + c = 0"""
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:  # Two real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2, "Two distinct real roots")
    
    elif discriminant == 0:  # One real root
        root = -b / (2*a)
        return (root, root, "One real root (repeated)")
    
    else:  # Two complex roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return (root1, root2, "Two complex roots")

# Example usage
a = 1
b = -3
c = 2

roots = quadratic_roots(a, b, c)
print(f"Root 1: {roots[0]}")
print(f"Root 2: {roots[1]}")
print(roots[2])