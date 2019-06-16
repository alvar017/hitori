import problema_espacio_estados as probee

import copy


class CrossOut(probee.Acción):

    def __init__(self, i, j):
        nombre = 'La fila {} y columna {}'.format(i, j)
        super().__init__(nombre)
        self.cell_row = i
        self.cell_colum = j

    # Indica si la casilla ya esta tachada
    def is_cross(self, estado):
        return not estado[self.cell_row][self.cell_colum]

    # Indica si existe el mismo numero en esa fila
    def exist_in_row(self, estado):
        return bool(estado[self.cell_row].count(estado[self.cell_row][self.cell_colum]) > 1)

    # Indica si existe el mismo numero en esa columna
    def exist_in_colum(self, estado):
        # Versión 1
        res = 0
        for i in range(len(estado)):
            if estado[i][self.cell_colum] == estado[self.cell_row][self.cell_colum]:
                res = res + 1
        aux = False
        if res > 1:
            aux = True
        return aux
        # Version 2
#        estado_traspuesta = [[estado[j][i] for j in range(len(estado))] for i in range(len(estado[0]))]
#        return bool(estado_traspuesta[self.cell_row].count(estado_traspuesta[self.cell_row][self.cell_colum]) > 1)

    # Indica si existe ya una casilla tachada en los alrededores
    def exist_black_cell_around(self, estado):
        aux = 0
        res = False

        if self.cell_row != 0 and self.cell_row != 0 and estado[self.cell_row-1][self.cell_colum] == 0:
            aux = aux + 1
        if aux == 0 and self.cell_colum != 0 and estado[self.cell_row][self.cell_colum-1] == 0:
            aux = aux + 1
        if aux == 0 and self.cell_colum != len(estado[self.cell_row])-1 and estado[self.cell_row][self.cell_colum+1] == 0:
            aux = aux + 1
        if aux == 0 and self.cell_row != len(estado)-1 and estado[self.cell_row+1][self.cell_colum] == 0:
            aux = aux + 1
        if aux > 0:
            res = True
        return res

    def is_corner(self, estado):
        res = False
        if self.cell_colum == 0 and self.cell_row == 0:
            res = True
        elif self.cell_colum == 0 and self.cell_row == len(estado)-1:
            res = True
        elif self.cell_colum == len(estado[0])-1 and self.cell_row == 0:
            res = True
        elif self.cell_colum == len(estado[0])-1 and self.cell_row == len(estado) - 1:
            res = True
        return res

    def is_lateral(self, estado):
        res = False
        if self.cell_colum == 0 or self.cell_colum == (len(estado[0]) - 1):
            res = True
        elif self.cell_row == 0 or self.cell_row == (len(estado) - 1):
            res = True
        return res

    # Indica si, al borrar una celda, si aisla con huecos alguna otra
    def check_isolate_cell(self, estado):
        res = False
        aux = self.get_croos_around(estado, self.cell_row, self.cell_colum)
        if self.is_corner(estado) and aux >= 2:
            res = True
        elif self.is_lateral(estado) and aux >= 3:
            res = True
        elif aux >= 4:
            res = True
        return res

    # Indica si el numero de huecos que rodea a una casilla
    def get_croos_around(self, estado, cellRow, cellColum):
        copy_estado = self.get_binary(estado)
        to_check = [[cellRow - 1, cellColum],
                    [cellRow, cellColum + 1],
                    [cellRow + 1, cellColum],
                    [cellRow, cellColum - 1]]
        to_check = list(filter(lambda x: x[0] >= 0 and x[1] >= 0, to_check))
        to_check = list(filter(lambda x: x[0] < (len(estado[self.cell_row])-0) and x[1] < (len(estado)-0), to_check))
        aux = 0
        for i in range(len(to_check)):
            aux = aux + copy_estado[to_check[i][0]][to_check[i][1]]
        return aux

    # Convierte el tablero a una variable binaria 0 o 1
    def get_binary(self, estado):
        copy_estado = copy.deepcopy(estado)
        for i in range(len(copy_estado[self.cell_row])):
            for j in range(len(copy_estado)):
                cell = copy_estado[i][j]
                if cell == 0:
                    copy_estado[i][j] = 1
                else:
                    copy_estado[i][j] = 0
        return copy_estado

    def check_black_cell_around(self, estado):
        valid_colum = list(filter(lambda x: x >= 0 and x < len(estado), [self.cell_row - 1, self.cell_row, 1 + self.cell_row]))
        valid_row = list(filter(lambda x: x >= 0 and x < len(estado), [self.cell_colum - 1, self.cell_colum, self.cell_colum + 1]))
        more_one_zero_row = len(list(filter(lambda x: estado[self.cell_row][x] == 0, valid_row))) > 0
        if not more_one_zero_row:
            return len(list(filter(lambda x: estado[x][self.cell_colum] == 0, valid_colum))) > 0
        else:
            return more_one_zero_row

        # Indica si, al borrar una celda, si aisla con huecos alguna otra

    def squareBetweenAPair(self,estado):
            res = False
            row = self.cell_row
            colum = self.cell_colum
            if(len(estado[0]) - colum >= 2 and colum >= 1):
                if(estado[row][colum - 1] == estado[row][colum + 1] and estado[row][colum] == 0):
                    res = True
            if (len(estado) - row >= 2 and row >= 1):
                if (estado[row + 1][colum] == estado[row - 1][colum] and estado[row][colum] == 0):
                    res = True
            return res

    def es_aplicable(self, estado):
        return not self.is_cross(estado) \
               and (self.exist_in_colum(estado) or self.exist_in_row(estado)) \
               and not self.exist_black_cell_around(estado) \
               and not self.check_isolate_cell(estado) \
               and not self.squareBetweenAPair(estado)

#               and not self.check_black_cell_around(estado)
#               Estos dos últimos métodos también funcionan pero van un poco más lento

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.cell_row][self.cell_colum] = 0
        return nuevo_estado

    def coste_de_aplicar(self, estado):
        return self.cell_row * -1000 + self.cell_colum * -100
















