import problema_espacio_estados as probee

import búsqueda_espacio_estados as busqee

import copy

estado1 = [{1,2,1},{2,2,1},{1,1,2}]

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
        res = 0
        for i in range(len(estado)):
            if estado[i][self.cell_colum] == estado[self.cell_row][self.cell_colum]:
                res = res + 1
        aux = False
        if res > 1:
            aux = True
        return aux

    def exist_black_cell_around(self, estado):
        aux = 0
        actual = estado[self.cell_row][self.cell_colum] == 0
        if self.cell_row != 0 and self.cell_row != 0 and estado[self.cell_row-1][self.cell_colum] == 0:
            aux = aux + 1
        if self.cell_colum != 0 and estado[self.cell_row][self.cell_colum-1] == 0:
            aux = aux + 1
        if self.cell_colum != len(estado[self.cell_row])-1 and estado[self.cell_row][self.cell_colum+1] == 0:
            aux = aux + 1
        if self.cell_row != len(estado)-1 and estado[self.cell_row+1][self.cell_colum] == 0:
            aux = aux + 1
        if actual and aux > 0:
            return True
        if aux == 4:
            return True
        if aux > 1 and (self.cell_row == 0 or self.cell_row == len(estado[self.cell_row])):
            return True
        if aux > 1 and (self.cell_colum == 0 or self.cell_colum == len(estado)):
            return True
        return False



if __name__ == '__main__':
    print("hola")
    estado1 = [[0,0,1],[1,1,1],[1,1,1]]
    print(estado1[1][1])
    pom = CrossOut(0,0)
    print(pom.exist_in_row(estado1))
    print(pom.exist_in_colum(estado1))
    print(pom.exist_black_cell_around(estado1))
















