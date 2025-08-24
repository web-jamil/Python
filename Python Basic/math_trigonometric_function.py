import math

# Trigonometric functions in the math module (angles are in radians)

print("--- Sine ---")
angle_rad = math.pi / 6  # 30 degrees in radians
print(f"Sine of {angle_rad:.4f} radians (30 degrees): {math.sin(angle_rad)}")

print("\n--- Cosine ---")
angle_rad = math.pi / 3  # 60 degrees in radians
print(f"Cosine of {angle_rad:.4f} radians (60 degrees): {math.cos(angle_rad)}")

print("\n--- Tangent ---")
angle_rad = math.pi / 4  # 45 degrees in radians
print(f"Tangent of {angle_rad:.4f} radians (45 degrees): {math.tan(angle_rad)}")

print("\n--- Arcsine (Inverse Sine) ---")
value = 0.5
arcsin_rad = math.asin(value)
print(f"Arcsine of {value} (in radians): {arcsin_rad:.4f}")
print(f"Arcsine of {value} (in degrees): {math.degrees(arcsin_rad):.2f}")

print("\n--- Arccosine (Inverse Cosine) ---")
value = 0.5
arccos_rad = math.acos(value)
print(f"Arccosine of {value} (in radians): {arccos_rad:.4f}")
print(f"Arccosine of {value} (in degrees): {math.degrees(arccos_rad):.2f}")

print("\n--- Arctangent (Inverse Tangent) ---")
value = 1
arctan_rad = math.atan(value)
print(f"Arctangent of {value} (in radians): {arctan_rad:.4f}")
print(f"Arctangent of {value} (in degrees): {math.degrees(arctan_rad):.2f}")

print("\n--- Arctangent of y/x (atan2) ---")
y = 4
x = 3
atan2_rad = math.atan2(y, x)
print(f"Arctangent of y={y}, x={x} (in radians): {atan2_rad:.4f}")
print(f"Arctangent of y={y}, x={x} (in degrees): {math.degrees(atan2_rad):.2f}")
# atan2 correctly handles the signs of both x and y to determine the quadrant.
y_neg = -4
atan2_rad_neg = math.atan2(y_neg, x)
print(f"Arctangent of y={y_neg}, x={x} (in radians): {atan2_rad_neg:.4f}")
print(f"Arctangent of y={y_neg}, x={x} (in degrees): {math.degrees(atan2_rad_neg):.2f}")

print("\n--- Converting Degrees to Radians ---")
angle_deg = 90
radians = math.radians(angle_deg)
print(f"{angle_deg} degrees in radians: {radians:.4f}")

print("\n--- Converting Radians to Degrees ---")
angle_rad = math.pi
degrees = math.degrees(angle_rad)
print(f"{angle_rad:.4f} radians in degrees: {degrees:.2f}")