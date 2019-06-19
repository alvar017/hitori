import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

from time import time

import auxiliar as auxiliar

import copy


class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, status):

        acciones = [investiga.CrossOut(i, j) for i in range(0, len(status)) for j in range(0, len(status[0]))]
        self.estado_inicial = status

        super().__init__(acciones, self.estado_inicial)


if __name__ == '__main__':

    start_time = time()

    status = [[8,6,2,1,4,4,3,2,7],[2,4,8,9,8,6,5,2,5],[4,8,9,7,2,4,6,6,3],[6,8,5,3,7,9,8,7,4],[7,7,4,8,5,2,7,3,9],[2,9,7,5,8,3,7,5,1],[6,5,6,5,1,7,2,8,1],[9,1,7,7,3,4,2,5,8],[4,3,1,5,9,8,4,7,6]]

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
            to_check_row = list(estado[i])
            zeros = zeros + 1 * to_check_row.count(0)
            row = row + 10000 * (len(to_check_row) - len(set(to_check_row)))
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

