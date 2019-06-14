import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

import copy

class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, estado):

        self.estado = estado
        acciones = self.aplicables()
        self.estado_inicial = self.estado

        estado_traspuesta = [[self.estado[j][i] for j in range(len(self.estado))] for i in range(len(self.estado[0]))]
        self.estado_traspuesta = estado_traspuesta

        super().__init__(acciones, self.estado_inicial)

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
    estado = [[0,2,0],[4,0,6],[0,8,0]]
    pom = hitori(estado)

    b_anchura = busqee.BúsquedaEnAnchura(detallado=True)
    acciones = [investiga.CrossOut(i, j) for i in range(0, 2) for j in range(0, 2) if i != j]
    hitori_resolver = probee.ProblemaEspacioEstados(acciones, pom.estado_inicial, None)
    print(b_anchura.buscar(hitori_resolver))
    print(hitori_resolver.es_estado_final(estado))


