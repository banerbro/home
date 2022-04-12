import math
z = int(input('дите градус угла:'))
n = math.radians(z)
x = math.cos(n)
x= math.degrees(x)
c = math.sin(n)
c = math.degrees(c)
v = math.tan(n)
v = math.degrees(v)
b = x/c
b = math.degrees(b)
print('синус,косинус,тангенс,котангенс:', x, c, v, b)