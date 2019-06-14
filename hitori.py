import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga

import copy

class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, estado):

        self.estado = estado
        acciones = [investiga.CrossOut(i, j) for i in range(0, len(estado)) for j in range(0, len(estado[0]))]
        self.estado_inicial = self.estado

        estado_traspuesta = [[self.estado[j][i] for j in range(len(self.estado))] for i in range(len(self.estado[0]))]
        self.estado_traspuesta = estado_traspuesta

        super().__init__(acciones, self.estado_inicial)

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
    estado = [[3,1,3,4],[1,2,4,3],[3,1,1,4],[3,4,2,4]]
    pom = hitori(estado)

    b_anchura = busqee.BúsquedaEnAnchura(detallado=True)
    acciones = [investiga.CrossOut(i, j) for i in range(0, len(pom.estado)) for j in range(0, len(pom.estado[0]))]
    hitori_resolver = probee.ProblemaEspacioEstados(acciones, pom.estado_inicial)
    print(b_anchura.buscar(hitori_resolver))


