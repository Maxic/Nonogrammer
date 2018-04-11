class Nonogram:

    def generateNonogramFromMatrix(self, matrix):
        return (self.generateNonogramRows(matrix), self.generateNonogramRows(matrix.transpose()))

    def generateNonogramRows(self, matrix):
        nonogramRows = []
        for row in matrix:
            count = 0
            rowNumbers = []
            for column in row:
                if column == 1:
                    count += 1
                elif count != 0:
                    rowNumbers.append(count)
                    count= 0
            if count != 0:
                rowNumbers.append(count)
            nonogramRows.append(rowNumbers)
        return nonogramRows