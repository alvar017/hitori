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
        filas = True
        columnas = True
        for i in range(len(estado)):
            to_check_row = list(filter(lambda x: x != 0, estado[i]))
            to_check_row_distinct = list(set(to_check_row))
            if len(to_check_row) != len(to_check_row_distinct):
                filas = False
                break
        estado_traspuesta = [[estado[j][i] for j in range(len(estado))] for i in range(len(estado[0]))]
        for i in range(len(estado_traspuesta)):
            to_check_row = list(filter(lambda x: x != 0, estado_traspuesta[i]))
            to_check_row_distinct = list(set(to_check_row))
            if len(to_check_row) != len(to_check_row_distinct):
                filas = False
                break
        res = filas & columnas
        if res:
            print("Solución")
            for i in range(len(estado)):
                print(estado[i])
            print("Solución")
        return res

    def acciones_aplicables(self, estado):
        return (acción
                for acción in self.acciones
                if acción.es_aplicable(estado))
