class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return ("{}, {}").format(self.x, self.y)

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return ("{}, {}").format(self.p1, self.p2)

    def dibujaLinea(self):
        print("dibujar Linea", self)
        
if __name__ == "__main__":
    punto1 = Punto(0, 0)
    punto2 = Punto(5, 5)
    linea = Linea(punto1, punto2)
    
    print(linea)
    linea.dibujaLinea()
