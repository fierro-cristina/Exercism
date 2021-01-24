class Matrix:
    def __init__(self, matrix_string):
        self.matrix_numbers = []
        matrix_rows = matrix_string.split("\n")
        for row in matrix_rows:
            row = row.split(' ')
            row = list(map(int, row))
            self.matrix_numbers.append(row)
        print(self.matrix_numbers)

    def row(self, index):
        return self.matrix_numbers[index-1]


    def column(self, index):
        col = []
        for row in self.matrix_numbers:
            col.append(row[index - 1])
        return col
