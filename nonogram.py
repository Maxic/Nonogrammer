from itertools import combinations
import numpy as np

class Nonogram:

    def generateNonogramFromMatrix(self, matrix):
        return (self.generateNonogramRows(matrix), self.generateNonogramRows(matrix.transpose()))

    def generateNonogramRows(self, matrix):
        nonogramRows = []
        for row in matrix:
            count = 0
            rowNumbers = []
            for index in row:
                if index:
                    count += 1
                elif count != 0:
                    rowNumbers.append(count)
                    count= 0
            if count != 0:
                rowNumbers.append(count)
            nonogramRows.append(rowNumbers)
        return nonogramRows

    def generatePossibleRows(self, rowDefinition, rowSize):
        numberClueSum = sum(rowDefinition)
        generatedRows = []

        for positions in combinations(range(rowSize), numberClueSum):
            p = [0] * rowSize
            for i in positions:
                p[i] = 1
            generatedRows.append(p)

        return generatedRows

    def checkRowIsValid(self, rowDefinition, row):

        count = 0
        rowNumbers = []
        for index in row:
            if index:
                count += 1
            elif count != 0:
                rowNumbers.append(count)
                count = 0
        if count != 0:
            rowNumbers.append(count)

        if rowNumbers.__eq__(rowDefinition):
            return True
        else:
            return False

    def solve(self, nonogramDefinition):
        rowDefinitions = nonogramDefinition[0]
        colDefinitions = nonogramDefinition[1]
        colSize = len(rowDefinitions)
        rowSize = len(rowDefinitions)

        count = 0
        for rowDefinition in rowDefinitions:
            count += 1
            possibleRows = self.generatePossibleRows(rowDefinition, rowSize )

            possibleValidRows = []
            for row in possibleRows:
                if self.checkRowIsValid(rowDefinition, row):
                    possibleValidRows.append(row)

            print("Possible rows for row: " + str(count))
            print(possibleValidRows)

        return True
