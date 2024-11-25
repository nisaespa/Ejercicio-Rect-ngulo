# Clase para el punto en el plano cartesiano (x,y)
class Punto:
    # Constructor 
    def __init__(self, x, y):
        self.x = x # Coordenada x
        self.y = y # Coordenada y
# Clase rectángulo
class Rectangulo:
    # Constructor que tiene como parametros el mètodo que se utilizarà y los argumentos del mismo
    def __init__(self, metodo, *args):
        # Sì el mètodo es 1, entonces
        if metodo == 1:
            # Se toma como argumentos a la esquina inferior izquierda como el punto, el ancho y el alto
            esquina_inferior_izquierda, ancho, alto = args
            # Atributos: ancho, alto y el centro
            self.ancho = ancho
            self.alto = alto
            # Para el centro llamamos a la clase Punto
            # Definimos la coordenada en x del centro que es la coordenada en x de la esquina inferior izquierda màs el ancho divido en 2.
            # Definimos la coordenada en y del centro que es la coordenada en y de la esquina inferior izquierda màs el alto divido en 2.
            self.centro = Punto(esquina_inferior_izquierda.x + ancho / 2, esquina_inferior_izquierda.y + alto / 2)
        # Sì el mètodo es 2, entonces
        elif metodo == 2:
            # Se toma como argumentos al centro como el punto, al ancho y el alto.
            centro, ancho, alto = args
            # Atributos: ancho, alto y el centro.
            self.ancho = ancho
            self.alto = alto
            self.centro = centro
        elif metodo == 3:
            # Se toma como argumentos las dos ezquinas opuestas del rectangulo.
            esquina_inferior_izquierda, esquina_superior_derecha = args
            # Fòrmula para el ancho
            self.ancho = esquina_superior_derecha.x - esquina_inferior_izquierda.x
            # Fòrmula para el alto
            self.alto = esquina_superior_derecha.y - esquina_inferior_izquierda.y
            # Fòrmula para el centro
            self.centro = Punto(esquina_inferior_izquierda.x + self.ancho / 2, esquina_inferior_izquierda.y + self.alto / 2)
        else:
            print("Escribe 1, 2 o 3 para seleccionar el mètodo.")
    # Funciòn para calcular el area.
    def calcular_area(self):
        return self.ancho * self.alto
    # Funciòn para calcular el perìmetro.
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)
    # Funciòn para verificar si un punto està dentro del rectàngulo
    def verificar_punto_dentro(self, punto):
        mitad_ancho = self.ancho / 2
        mitad_alto = self.alto / 2
        return (self.centro.x - mitad_ancho <= punto.x <= self.centro.x + mitad_ancho and self.centro.y - mitad_alto <= punto.y <= self.centro.y + mitad_alto)
# Clase Cuadrado que hereda los atributos de Rectangulo.    
class Cuadrado(Rectangulo):
    def __init__(self, centro, lado):
        super().__init__(2, centro, lado, lado)
# Iniciamos el programa
if __name__=="__main__":
    # Definimos que argumentos tendrà la clase Rectàngulo
    rectangulo = Rectangulo(2, Punto(0, 0), 4, 6)
    # Imprimimos el area y el perìmetro.
    print("El àrea del rectángulo es:", rectangulo.calcular_area(), "cm^2")
    print("El perímetro del rectángulo es:", rectangulo.calcular_perimetro(), "cm")
    # Definimos el punto que queremos verificar dentro del rectangulo
    punto = Punto(2, 3)
    print("el punto està dentro del rectàngulo: ", rectangulo.verificar_punto_dentro(punto))
    # Definimos que argumentos tendrà la clase Cuadrado
    cuadrado = Cuadrado(Punto(5, 5), 4)
    print("Área del cuadrado:", cuadrado.calcular_area(), "cm^2")
    print("Perímetro del cuadrado:", cuadrado.calcular_perimetro(), "cm")
