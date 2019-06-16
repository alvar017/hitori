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


