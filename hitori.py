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
#        status = auxiliar.Auxiliar.inserta_matriz(None)
#        resolucion = auxiliar.Auxiliar.elige_algoritmo(None)
        # Interactivo

        # Programatico
        status = [[5,1,6,4,9,8,2,4,3],[7,6,4,3,4,8,2,9,3],[3,8,1,2,6,3,7,5,4],[6,2,4,8,1,1,3,7,3],[2,6,7,8,8,5,9,4,6],[1,9,5,7,8,6,3,1,2],[9,7,7,1,5,4,8,2,7],[7,1,9,3,2,7,5,6,8],[6,4,3,9,7,2,1,7,5]]
        resolucion = 4
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

