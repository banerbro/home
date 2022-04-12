import math
z = int(input('дите градус угла:'))
n = math.radians(z)
x = math.cos(n)
c = math.sin(n)
v = c/x
b = x/c
print('косинус,синус,тангенс,котангенс:', x, c, v, b)