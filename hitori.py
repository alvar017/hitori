import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

from time import time

import auxiliar as auxiliar

from scipy.ndimage import label

import copy


class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, status):

        acciones = [investiga.CrossOut(i, j) for i in range(0, len(status)) for j in range(0, len(status[0]))]
        self.estado_inicial = status

        super().__init__(acciones, self.estado_inicial)


if __name__ == '__main__':

    status = []
    n = input("Intruduzca su matriz a resolver: ")
    n = list(n.split("],["))
    for i in range(len(n)):
        if i == 0:
            n[0] = n[0][2:]
        if i == len(n)-1:
            n[i] = n[i][:-2]
        n[i].replace("[", "")
    for i in range(len(n)):
        cells = []
        aux = n[i].split(",")
        for j in range(len(aux)):
            cells.append(int(aux[j]))
        status.append(cells)

    resolucion = 9

    while resolucion == 9:
        n = (input(
            '\nSeleccione algoritmo de búsqueda\n' +
            '1: Búsqueda en Anchura,\n'
            '2: Búsqueda en Profundidad,\n'
            '3: Búsqueda óptima,\n'
            '4: Búsqueda A*,\n'
            'Cualquier otro parámetro para salir\n'
            'Decisión:'))
        if n == '1':
            resolucion = 1
        elif n == '2':
            resolucion = 2
        elif n == '3':
            resolucion = 3
        elif n == '4':
            resolucion = 4
        else:
            print("Solución no válida. Recuerde que debe introducir un número entre 1 y 4")
            resolucion = 9


#    status = [[1,8,2,4,3,9,4,1,5],[6,5,5,1,1,4,9,3,3],[8,4,6,9,5,3,2,6,7],[4,8,3,8,7,8,8,2,9],[1,6,4,2,3,6,5,9,1],[9,5,8,3,5,2,7,6,1],[2,5,3,1,6,4,4,2,8],[5,4,4,2,9,3,7,7,6],[7,9,1,5,1,6,3,8,8]]

    start_time = time()
    statusChange = auxiliar.Auxiliar.adjacent_triplet(status)

    print(statusChange)

    statusChangeTras = [[statusChange[j][i] for j in range(len(statusChange))] for i in range(len(statusChange[0]))]

    print(statusChangeTras)

    statuschange2 = auxiliar.Auxiliar.pair_induction(statusChange, statusChangeTras)

    print(statuschange2)

    pom = hitori(statuschange2)
    hitori_resolver = probee.ProblemaEspacioEstados(pom.acciones, pom.estado_inicial)

    print(len(pom.acciones))
    print(pom.acciones)

    if resolucion == 1:
        # Búsqueda en anchura
        b_anchura = busqee.BúsquedaEnAnchura(detallado=True)
        print(b_anchura.buscar(hitori_resolver))
    elif resolucion == 2:
        # Búsqueda en profundidad
        b_profundidad = busqee.BúsquedaEnProfundidad(detallado=True)
        print(b_profundidad.buscar(hitori_resolver))
    elif resolucion == 3:
        # Búsqueda óptima
        b_óptima = busqee.BúsquedaÓptima(detallado=True)
        print(b_óptima.buscar(hitori_resolver))
    elif resolucion == 4:
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

