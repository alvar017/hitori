import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

import copy

class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, estado):

        self.estado = estado
        acciones = self.aplicables()
        estado_inicial = self.estado

        print("Estado inicial")
        print(estado_inicial)
        print("Estado inicial")

        estado_traspuesta = [[self.estado[j][i] for j in range(len(self.estado))] for i in range(len(self.estado[0]))]
        self.estado_traspuesta = estado_traspuesta

        print("Normal")
        print(estado[0])
        print(estado[1])
        print(estado[2])
        print("Normal")
        print("Traspuesta")
        print(self.estado_traspuesta[0])
        print(self.estado_traspuesta[1])
        print(self.estado_traspuesta[2])
        print("Traspuesta")
        print("Acciones")

        for i in range(len(acciones)):
            print("UN ESTADO INICIO")
            print(acciones[i])
            print("UN ESTADO FIN")
        print("Acciones")

        super().__init__(acciones, estado_inicial)

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

    def aplicables(self):
        acciones = []
        x = 0
        for i in range(len(self.estado)):
            for j in range(len(self.estado[0])):
                if (self.estado[i][j] != 0):
                    copy_estado = copy.deepcopy(self.estado)
                    copy_estado[i][j] = 0
                    acciones.append(copy_estado)
                    x = x + 1
        return acciones

if __name__ == '__main__':
    estado = [[1,2,1],[2,2,1],[3,1,2]]
    pom = hitori(estado)

    b_anchura = busqee.BúsquedaEnAnchura(detallado=True)
    b_anchura.buscar(hitori)


