class Acción:
    def __init__(self, nombre='', aplicabilidad=None, aplicación=None,
                 coste=None):
        self.nombre = nombre
        self.aplicabilidad = aplicabilidad
        self.aplicación = aplicación
        self.coste = coste

    def es_aplicable(self, estado):
        if self.aplicabilidad is None:
            raise NotImplementedError(
                'Aplicabilidad de la acción no implementada')
        else:
            return self.aplicabilidad(estado)

    def aplicar(self, estado):
        if self.aplicar is None:
            raise NotImplementedError(
                'Aplicación de la acción no implementada')
        else:
            return self.aplicación(estado)

    def coste_de_aplicar(self, estado):
        if self.coste is None:
            return 1
        else:
            return self.coste(estado)

    def __str__(self):
        return 'Acción: {}'.format(self.nombre)


class ProblemaEspacioEstados:
    def __init__(self, acciones, estado_inicial=None):
        if not isinstance(acciones, list):
            raise TypeError('Debe proporcionarse una lista de acciones')
        self.acciones = acciones
        self.estado_inicial = estado_inicial

    def es_estado_final(self, estado):
        accion = self.acciones[len(self.acciones)-1]
        check = (len(estado) - 1) == accion.cell_row and (len(estado[0]) - 1) == accion.cell_colum
        if check:
            filas = True
            columnas = True
            for i in range(len(estado)):
                to_check_row = list(filter(lambda x: x != 0, estado[i]))
                to_check_row_distinct = list(set(to_check_row))
                if len(to_check_row) != len(to_check_row_distinct):
                    filas = False
                    break
                columnasAux = []
                for j in range(len(estado[0])):
                    columnasAux.append(estado[i][j])
                to_check_colum = list(filter(lambda x: x != 0, columnasAux))
                to_check_colum_distinct = list(set(to_check_colum))
                if len(to_check_colum) != len(to_check_colum_distinct):
                    columnas = False
                    break
            return filas & columnas
        else:
            return False

    def acciones_aplicables(self, estado):
        return (acción
                for acción in self.acciones
                if acción.es_aplicable(estado))
