import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

from time import time

class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, estado):

        self.estado = estado
        acciones = [investiga.CrossOut(i, j) for i in range(0, len(estado)) for j in range(0, len(estado[0]))]
        self.estado_inicial = self.estado
        self.estado_traspuesta = [[self.estado[j][i] for j in range(len(self.estado))] for i in range(len(self.estado[0]))]

        super().__init__(acciones, self.estado_inicial)

if __name__ == '__main__':
    tiempo_inicial = time()

    estado = [[1,8,2,4,3,9,4,1,5],[6,5,5,1,1,4,9,3,3],[8,4,6,9,5,3,2,6,7],[4,8,3,8,7,8,8,2,9],[1,6,4,2,3,6,5,9,1],[9,5,8,3,5,2,7,6,1],[2,5,3,1,6,4,4,2,8],[5,4,4,2,9,3,7,7,6],[7,9,1,5,1,6,3,8,8]]

    def adjacentTriplet(estado):
        newEstado = estado
        for j in range(len(newEstado[0])):
            for i in range(len(newEstado)):
               if(len(estado) - i >= 3):
                     if newEstado[i][j] == newEstado[i+1][j] == newEstado[i+2][j]:
                        print("Entro en el if")
                        newEstado[i][j] = 0
                        newEstado[i+2][j] = 0
        for i in range(len(newEstado)):
            for j in range(len(newEstado[0])):
                if (len(estado[0]) - j >= 3):
                    if newEstado[i][j] == newEstado[i][j+1] == newEstado[i][j+2]:
                        print("Entro en el if")
                        newEstado[i][j] = 0
                        newEstado[i][j+2] = 0
        return newEstado


    estadoChange = adjacentTriplet(estado)

    print(estadoChange)

    pom = hitori(estadoChange)
    hitori_resolver = probee.ProblemaEspacioEstados(pom.acciones, pom.estado_inicial)
    print(len(pom.acciones))
    print(pom.acciones)


    def squareBetweenAPair(estado):
        res = False
        for j in range(len(estado[0])):
            for i in range(len(estado)):
                if (len(estado) - i >= 2):
                    if estado[i - 1][j] == estado[i + 1][j] and estado[i][j] == 0:
                        res = True
                        break
        for i in range(len(estado)):
            for j in range(len(estado[0])):
                if (len(estado[0]) - j >= 2):
                    if estado[i][j - 1] == estado[i][j + 1] and estado[i][j] == 0:
                        res = True
                        break
        return res

    # Búsqueda en anchura

#    b_anchura = busqee.BúsquedaEnAnchura(detallado=True)
#    print(b_anchura.buscar(hitori_resolver))

    # Búsqueda en profundidad

#    b_profundidad = busqee.BúsquedaEnProfundidad(detallado=True)
#    print(b_profundidad.buscar(hitori_resolver))

    # Búsqueda óptima

#    b_óptima = busqee.BúsquedaÓptima(detallado=True)
#    print(b_óptima.buscar(hitori_resolver))

    # Búsqueda A*

    def h(nodo):
        estado = nodo.estado
        row = 100000000000000
        zeros = 0
     #   square = squareBetweenAPair(estado)
      #  if (square == False):
       #     zeros = zeros + 1000
        for i in range(len(estado)):
            to_check_row = list(filter(lambda x: x != 0, estado[i]))
            for j in range(len(estado[0])):
                if estado[i][j] == 0:
                    zeros = zeros + 25
            row = row - 100 * len(list(set(to_check_row)))
        return row - 10000 * zeros

    b_a_estrella = busqee.BúsquedaAEstrella(h)
    print(b_a_estrella.buscar(hitori_resolver))

tiempo_final = time()

tiempo_ejecucion = tiempo_final - tiempo_inicial

print("La ejecución ha tardado: ")
print(tiempo_ejecucion)

