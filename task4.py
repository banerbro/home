def mathhelp():
    z = int(input('Угол'))
    x = radians(cos(z))
    c = radians(sin(z))
    v = radians(tan(z))
    b = radians(ctan(z))
    print('Косинус', x)
    print('Синус', c)
    print('Тангенс', v)
    print('Котангенс', b)
mathhelp()