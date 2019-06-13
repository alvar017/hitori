import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

import copy

class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, estado):
        super().__init__(estado)
        self.estado = estado

    def es_estado_final(self, estado):
        filas = True
        columnas = True
        print(estado)
        for i in range(len(estado)):
            to_check_row = list(filter(lambda x: x!=0, estado[i]))
            to_check_row_distinct = list(set(to_check_row))
            if(len(to_check_row) != len(to_check_row_distinct)):
               filas = False
               break
        for i in range(len(estado[0])):
            to_check_colum = list(filter(lambda x: x!=0, estado[i]))
            to_check_colum_distinct = list(set(to_check_row))
            if(len(to_check_row) != len(to_check_row_distinct)):
               filas = False
               break
        return filas & columnas

if __name__ == '__main__':
    estado = [[1, 2, 3, 4], [1, 2, 3, 4], [2, 5, 6, 7], [3, 0, 6, 2]]
    pom = hitori(estado)
    print(pom.es_estado_final(pom.estado))

