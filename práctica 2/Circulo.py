class Punto:
    def __init__(self, c, r):
        self.c = c
        self.r = r

    def __str__(self):
        return "{}, {}".format(self.c, self.r)

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return "Circulo({}, {}, radio={})".format(self.centro.c, self.centro.r, self.radio)

    def dibuja_circulo(self):
        print("Dibujando un círculo en {} con radio {}".format(self.centro, self.radio))

centro = Punto(5, 10)
circulo = Circulo(centro, 3.5)
print(circulo)
circulo.dibuja_circulo()
