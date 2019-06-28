
from time import time

import auxiliar as auxiliar

import hitori as hitori

import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

if __name__ == '__main__':

    start_time = time()
    archivo = open('C:/Users/anton/Documentos/IA/hitori/ejemplos_prueba.txt')

    # Lee todas la líneas y asigna a lista
    lista = archivo.readlines()

    # Inicializa un contador
    numlin = 0

    # Recorre todas los elementos de la lista
    for linea in lista:
        start_time1 = time()
        # incrementa en 1 el contador
        numlin += 1

        if(numlin == 63):
            numlin += 1
        # muestra contador y elemento (línea)
        print(numlin, linea)

        linea = eval(linea)

        status = linea

        resolucion = 4



        statusChange = auxiliar.Auxiliar.adjacent_triplet(status)
        statusChangeTras = [[statusChange[j][i] for j in range(len(statusChange))] for i in range(len(statusChange[0]))]
        #    statuschange2 = auxiliar.Auxiliar.pair_induction(statusChange, statusChangeTras)
        statusTry2Next = auxiliar.Auxiliar.twoNext(statusChange)
        #    newStateMultipleCopy = copy.deepcopy(statusTry2Next)

        res = auxiliar.Auxiliar.multipleCero(statusTry2Next)
        while res:
            res = auxiliar.Auxiliar.multipleCero(statusTry2Next)

        pom = hitori.hitori(statusTry2Next)
        hitori_resolver = probee.ProblemaEspacioEstados(pom.acciones, pom.estado_inicial)

        numberRepeats = 0
        numberRepeats = auxiliar.Auxiliar.repeatsNumber(statusTry2Next)

        if resolucion == 4:
            # Búsqueda A*
            print("\nRealizando la búsqueda, sea paciente por favor.\n")


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

        finish_time1 = time()
        execute_time2 = finish_time1 - start_time1
        print("\nLa ejecución ha tardado: {}\n".format(execute_time2))


    archivo.close  # cierra archivo
    finish_time2 = time()
    execute_time3 = finish_time2 - start_time
    print("\nLa ejecución total del archivo ha tardado: {}\n".format(execute_time3))

