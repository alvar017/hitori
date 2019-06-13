import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

import copy

class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, estado):
        super().__init__(estado)
        self.estado = estado
        estado_traspuesta = [[self.estado[j][i] for j in range(len(self.estado))] for i in range(len(self.estado[0]))]
        self.estado_traspuesta = estado_traspuesta
        print("Normal")
        print(estado[0])
        print(estado[1])
        print(estado[2])
        print(estado[3])
        print("Normal")
        print("Traspuesta")
        print(self.estado_traspuesta[0])
        print(self.estado_traspuesta[1])
        print(self.estado_traspuesta[2])
        print(self.estado_traspuesta[3])
        print("Traspuesta")

    def es_estado_final(self):
        filas = True
        columnas = True
        for i in range(len(self.estado)):
            to_check_row = list(filter(lambda x: x!=0, self.estado[i]))
            to_check_row_distinct = list(set(to_check_row))
            if len(to_check_row) != len(to_check_row_distinct):
               filas = False
               break
        for i in range(len(self.estado_traspuesta)):
            to_check_colum = list(filter(lambda x: x!=0, self.estado_traspuesta[i]))
            to_check_colum_distinct = list(set(to_check_colum))
            if len(to_check_colum) != len(to_check_colum_distinct):
               filas = False
               break
        return filas & columnas

if __name__ == '__main__':
    estado = [[1, 2, 3, 4], [7, 1, 8, 9], [2, 5, 6, 7], [3, 0, 5, 2]]
    pom = hitori(estado)
    print(pom.es_estado_final())

