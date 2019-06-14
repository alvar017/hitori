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

#    b_profundidad = busqee.BúsquedaEnProfundidad(detallado=True)
#    print(b_profundidad.buscar(hitori_resolver))

    # Búsqueda óptima

#    b_óptima = busqee.BúsquedaÓptima()
#    print(b_óptima.buscar(hitori_resolver))

    # Búsqueda A*

    def h(nodo):
        estado = nodo.estado
        row = 100000000000000
        zeros = 0
        for i in range(len(estado)):
            to_check_row = list(filter(lambda x: x != 0, estado[i]))
            for j in range(len(estado[0])):
                if estado[i][j] == 0:
                    zeros = zeros + 1
            row = row - 100 * len(list(set(to_check_row)))
        return row - 10000 * zeros

    b_a_estrella = busqee.BúsquedaAEstrella(h)
    print(b_a_estrella.buscar(hitori_resolver))


