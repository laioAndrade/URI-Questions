import math

pi = 3.14159
x = input().split(" ")
a = float(x[0])
b = float(x[1])
c = float(x[2])

triangle = (a*c)/2
circle = pi*math.pow(c,2)
trapezium = ((a+b)*c)/2
square = math.pow(b,2)
rectangle = a*b

print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" %(triangle, circle, trapezium, square, rectangle))