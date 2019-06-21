import copy


class Auxiliar():

    def __init__(self, estado):

        self.estado = self.adjacent_triplet(estado)
        self.estado2 = self.square_between_a_pair(estado)

    def adjacent_triplet(status):
        new_status = status
        for j in range(len(new_status[0])):
            for i in range(len(new_status)):
                if len(status) - i >= 3:
                    if new_status[i][j] == new_status[i+1][j] == new_status[i+2][j]:
                        print("Entro en el if")
                        new_status[i][j] = 0
                        new_status[i+2][j] = 0
        for i in range(len(new_status)):
            for j in range(len(new_status[0])):
                if len(status[0]) - j >= 3:
                    if new_status[i][j] == new_status[i][j+1] == new_status[i][j+2]:
                        print("Entro en el if")
                        new_status[i][j] = 0
                        new_status[i][j+2] = 0
        return new_status

    def square_between_a_pair(status):
        res = False
        for j in range(len(status[0])):
            for i in range(len(status)):
                if len(status) - i >= 2:
                    if status[i - 1][j] == status[i + 1][j] and status[i][j] == 0:
                        res = True
                        break
        for i in range(len(status)):
            for j in range(len(status[0])):
                if len(status[0]) - j >= 2:
                    if status[i][j - 1] == status[i][j + 1] and status[i][j] == 0:
                        res = True
                        break
        return res

    def pair_induction(estado, estado_traspuesta):
        estado_copy = copy.deepcopy(estado)
        for i in range(len(estado)):
            for j in range(len(estado[0])):
                aux = []
                valid_colum_in_row = list(filter(lambda x: 0 <= x < len(estado[0]), [j, j+1, j + 2, j + 3]))
                for f in valid_colum_in_row:
                    aux.append(estado[i][f])
                if aux.count(estado[i][j]) == 3 and estado[i][j] != 0:
                    if aux[0] == aux[1] == aux[3]:
                      estado_copy[i][j+3] = 0
                    if aux[0] == aux[2] == aux[3]:
                        estado_copy[i][j] = 0
        for i in range(len(estado_traspuesta)):
            for j in range(len(estado_traspuesta[0])):
                aux = []
                valid_colum_in_row = list(filter(lambda x: 0 <= x < len(estado_traspuesta[0]), [j, j+1, j + 2, j + 3]))
                for f in valid_colum_in_row:
                    aux.append(estado_traspuesta[i][f])
                if aux.count(estado_traspuesta[i][j]) == 3 and estado_traspuesta[i][j] != 0:
                    if aux[0] == aux[1] == aux[3]:
                        estado_copy[j + 3][i] = 0
                    if aux[0] == aux[2] == aux[3]:
                        estado_copy[j][i] = 0
        return estado_copy
