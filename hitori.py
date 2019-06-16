import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

from time import time

import auxiliar as auxiliar

import copy

class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, status):

        self.status = status
        acciones = [investiga.CrossOut(i, j) for i in range(0, len(status)) for j in range(0, len(status[0]))]
        self.estado_inicial = self.status
        self.estado_traspuesta = [[self.status[j][i] for j in range(len(self.status))] for i in range(len(self.status[0]))]

        super().__init__(acciones, self.estado_inicial)


if __name__ == '__main__':

    start_time = time()

    status = [[3,4,5,5,1,3],[5,6,2,3,2,1],[5,3,1,4,5,4],[1,4,3,4,2,2],[3,1,6,1,4,5],[1,2,1,5,3,4]]

    statusChange = auxiliar.Auxiliar.adjacent_triplet(status)

    print(statusChange)

    pom = hitori(statusChange)
    hitori_resolver = probee.ProblemaEspacioEstados(pom.acciones, pom.estado_inicial)

    print(len(pom.acciones))
    print(pom.acciones)

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
        for i in range(len(estado)):
            to_check_row = list(filter(lambda x: x != 0, estado[i]))
            for j in range(len(estado[0])):
                if estado[i][j] == 0:
                    zeros = zeros + 10
            row = row - 10000 * len(set(to_check_row))
        square = auxiliar.Auxiliar.square_between_a_pair(estado)
        if square:
            zeros = 0
        return row - 10000 * zeros

    b_a_estrella = busqee.BúsquedaAEstrella(h)
    print(b_a_estrella.buscar(hitori_resolver))

finish_time = time()

execute_time = finish_time - start_time

print("La ejecución ha tardado: ")
print(execute_time)

