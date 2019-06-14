import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import investiga as investiga


class hitori(probee.ProblemaEspacioEstados):
    def __init__(self, estado):

        self.estado = estado
        acciones = [investiga.CrossOut(i, j) for i in range(0, len(estado)) for j in range(0, len(estado[0]))]
        self.estado_inicial = self.estado
        self.estado_traspuesta = [[self.estado[j][i] for j in range(len(self.estado))] for i in range(len(self.estado[0]))]

        super().__init__(acciones, self.estado_inicial)

if __name__ == '__main__':
    estado = [[3,4,5,5,1,3],[5,6,2,3,2,1],[5,3,1,4,5,4],[1,4,3,4,2,2],[3,1,6,1,4,5],[1,2,1,5,3,4]]
    pom = hitori(estado)
    hitori_resolver = probee.ProblemaEspacioEstados(pom.acciones, pom.estado_inicial)

    # Búsqueda en anchura

#    b_anchura = busqee.BúsquedaEnAnchura(detallado=True)
#    print(b_anchura.buscar(hitori_resolver))

    # Búsqueda en profundidad

    b_profundidad = busqee.BúsquedaEnProfundidad(detallado=True)
    print(b_profundidad.buscar(hitori_resolver))



