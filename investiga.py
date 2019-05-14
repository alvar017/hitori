import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import copy

estado1 = [{1,2,1},{2,2,1},{3,1,2}]

class CrossOut(probee.Acción):
    def __init__(self,i,j):
        nombre= 'La fila {} y columna {}'.format(i,j)
        super().__init__(nombre)
        self.cell_row = i
        self.cell_colum = j


    def is_cross(self,estado,cell):
        return not bool(estado[cell])

    def exist_in_row(self,estado):
        return  bool(estado[self.cell_row].count(estado[self.cell_row][self.cell_colum]) > 1)

    def exist_in_colum(self, estado):
        return bool(estado[self.cell_colum].count(estado[self.cell_row][self.cell_colum]) > 1)



if __name__ == '__main__':
    print("hola")
    estado1 = [[1,2,1],[2,2,1],[3,1,2]]
    print(estado1[0][0])
    pom = CrossOut(0,0)
    print(pom.exist_in_row(estado1))
    print(pom.exist_in_colum(estado1))
















