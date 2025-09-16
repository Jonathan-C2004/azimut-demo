
import math

def azimut(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle_rad = math.atan2(dx, dy)
    angle_deg = math.degrees(angle_rad)
    return angle_deg % 360

# Solicitar coordenadas al usuario
x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))

print(f"Azimut de P1 a P2: {azimut(x1, y1, x2, y2):.2f}°")

