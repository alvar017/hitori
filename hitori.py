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

    status = [[3,1,3,2,6,4],[1,2,6,3,3,5],[3,1,1,5,4,1],[3,4,2,6,3,3],[2,6,3,1,5,4],[2,5,3,1,2,4]]

    statusChange = auxiliar.Auxiliar.adjacent_triplet(status)

    print(statusChange)

    statusChangeTras =  [[statusChange[j][i] for j in range(len(statusChange))] for i in range(len(statusChange[0]))]

    print(statusChangeTras)

    statuschange2 = auxiliar.Auxiliar.pair_induction(statusChange, statusChangeTras)

    print(statuschange2)

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

