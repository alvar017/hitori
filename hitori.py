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

    repetir = "si"
    while repetir == "si":
        # Interactivo
        status = auxiliar.Auxiliar.inserta_matriz(None)
        resolucion = auxiliar.Auxiliar.elige_algoritmo(None)
        # Interactivo

        # Programatico
#        status = [[12, 11, 14, 13, 10, 8, 20, 10, 18, 6, 18, 10, 3, 1, 6, 15, 5, 10, 9, 1],[19, 12, 12, 16, 1, 17, 5, 3, 3, 6, 17, 11, 8, 4, 20, 6, 9, 7, 2, 6],[16, 20, 8, 2, 5, 6, 17, 11, 9, 1, 8, 8, 7, 12, 4, 4, 14, 18, 10, 16],[1, 4, 10, 12, 5, 20, 8, 6, 18, 9, 19, 2, 8, 15, 17, 1, 18, 11, 7, 5],[8, 9, 2, 19, 6, 7, 2, 5, 17, 12, 10, 16, 19, 14, 16, 13, 20, 1, 15, 12],[5, 5, 4, 16, 7, 14, 1, 6, 7, 1, 4, 8, 2, 6, 15, 12, 8, 16, 11, 18],[14, 14, 1, 11, 2, 17, 9, 16, 13, 8, 8, 10, 1, 19, 17, 7, 18, 18, 20, 6],[17, 15, 4, 8, 9, 9, 4, 12, 20, 17, 13, 14, 1, 13, 18, 3, 16, 2, 3, 19],[3, 16, 17, 16, 12, 4, 14, 3, 4, 15, 6, 17, 9, 20, 2, 3, 16, 13, 14, 8],[5, 7, 16, 15, 10, 3, 6, 1, 3, 2, 11, 4, 13, 9, 10, 8, 11, 16, 13, 20],[9, 13, 10, 17, 9, 11, 14, 18, 6, 2, 1, 19, 8, 5, 5, 2, 7, 12, 12, 10],[13, 18, 20, 5, 3, 10, 12, 1, 17, 3, 19, 16, 15, 2, 9, 13, 7, 4, 1, 6],[18, 6, 8, 1, 15, 2, 13, 9, 4, 16, 3, 6, 17, 5, 16, 14, 8, 20, 17, 2],[4, 14, 9, 18, 18, 1, 9, 1, 12, 3, 7, 16, 5, 13, 10, 17, 4, 15, 19, 6],[10, 12, 4, 12, 18, 19, 15, 13, 8, 14, 12, 7, 20, 13, 11, 19, 6, 3, 12, 1],[6, 16, 5, 3, 16, 18, 10, 17, 8, 7, 15, 12, 10, 11, 1, 2, 13, 3, 8, 9],[2, 10, 18, 5, 8, 15, 2, 4, 1, 4, 11, 8, 16, 3, 13, 9, 9, 14, 6, 6],[19, 17, 11, 19, 20, 13, 16, 7, 3, 10, 14, 15, 6, 5, 8, 4, 2, 1, 12, 4],[4, 6, 15, 7, 2, 2, 6, 20, 10, 17, 2, 1, 13, 8, 12, 16, 15, 5, 2, 11],[2, 1, 13, 6, 4, 10, 19, 14, 7, 18, 20, 13, 17, 5, 3, 19 ,12, 8, 5, 15]]
#        resolucion = 4
        # Programatico

        auxiliar.Auxiliar.imprime_solucion(status, "Tablero hitori propuesto")
        start_time1 = time()

        statusChange = auxiliar.Auxiliar.adjacent_triplet(status)
        statusChangeTras = [[statusChange[j][i] for j in range(len(statusChange))] for i in range(len(statusChange[0]))]
    #    statuschange2 = auxiliar.Auxiliar.pair_induction(statusChange, statusChangeTras)
        statusTry2Next = auxiliar.Auxiliar.twoNext(statusChange)
    #    newStateMultipleCopy = copy.deepcopy(statusTry2Next)

        res = auxiliar.Auxiliar.multipleCero(statusTry2Next)
        while res:
            res = auxiliar.Auxiliar.multipleCero(statusTry2Next)

        pom = hitori(statusTry2Next)
        hitori_resolver = probee.ProblemaEspacioEstados(pom.acciones, pom.estado_inicial)

        numberRepeats = 0
        numberRepeats = auxiliar.Auxiliar.repeatsNumber(statusTry2Next)

        finish_time1 = time()
        execute_time1 = finish_time1 - start_time1

    #    print(statusChange)
    #    print(statusChangeTras)
    #    print(statuschange2)
    #    print(statusTry2Next)
    #    print(newStateMultipleCopy)
    #    print(len(pom.acciones))
    #    print(pom.acciones)
    #    print("numberRepeats")
    #    print(numberRepeats)
    #    print("numberRepeats")

        if resolucion == 1:
            # Búsqueda en anchura
            detallado = auxiliar.Auxiliar.detallado(None)
            start_time2 = time()

            b_anchura = busqee.BúsquedaEnAnchura(detallado)
            b_anchura.buscar(hitori_resolver)

            finish_time2 = time()
            execute_time2 = finish_time2 - start_time2
            execute_time = execute_time1 + execute_time2

        elif resolucion == 2:
            # Búsqueda en profundidad
            detallado = auxiliar.Auxiliar.detallado(None)
            start_time2 = time()

            b_profundidad = busqee.BúsquedaEnProfundidad(detallado)
            b_profundidad.buscar(hitori_resolver)

            finish_time2 = time()
            execute_time2 = finish_time2 - start_time2
            execute_time = execute_time1 + execute_time2

        elif resolucion == 3:
            # Búsqueda óptima
            detallado = auxiliar.Auxiliar.detallado(None)
            start_time2 = time()

            b_óptima = busqee.BúsquedaÓptima(detallado)
            b_óptima.buscar(hitori_resolver)

            finish_time2 = time()
            execute_time2 = finish_time2 - start_time2
            execute_time = execute_time1 + execute_time2

        elif resolucion == 4:
            # Búsqueda A*
            print("\nRealizando la búsqueda, sea paciente por favor.\n")
            start_time2 = time()

            def h(nodo):
                estado = nodo.estado
                row = 100000000000000
                zeros = 0
                numberRepeatsNode = auxiliar.Auxiliar.repeatsNumber(estado)
    #            for i in range(len(estado)):
    #                to_check_row = list(estado[i])
    #                zeros = zeros + 1 * to_check_row.count(0)
    #                row = row - 10000 * len(set(to_check_row))
                square = auxiliar.Auxiliar.square_between_a_pair(estado)
                if square:
                    zeros = 0
                row = row + 10000 * numberRepeatsNode
                return row - 10000 * zeros

            b_a_estrella = busqee.BúsquedaAEstrella(h)
            b_a_estrella.buscar(hitori_resolver)

            finish_time2 = time()
            execute_time2 = finish_time2 - start_time2
            execute_time = execute_time1 + execute_time2

        print("\nLa ejecución ha tardado: {}\n".format(execute_time))
        if repetir == "si":
            repetir = input("¿Desea realizar otra búsqueda? Escriba si para continuar o cualquier otra tecla para salir: ")
        if repetir != "si":
            print("¡Hasta luego!")

