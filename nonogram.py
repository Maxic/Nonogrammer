from itertools import combinations


class Nonogram:
    def generate_nonogram_from_matrix(self, matrix):
        return self.generate_nonogram_rows(matrix), self.generate_nonogram_rows(matrix.transpose())

    @staticmethod
    def generate_nonogram_rows(matrix):
        nonogram_rows = []
        for row in matrix:
            count = 0
            row_numbers = []
            for index in row:
                # Value that's not filled in is either 0 or None
                if index:
                    count += 1
                elif count != 0:
                    row_numbers.append(count)
                    count = 0
            if count != 0:
                row_numbers.append(count)
            nonogram_rows.append(row_numbers)
        return nonogram_rows

    @staticmethod
    def generate_possible_rows(row_definition, row_size):
        number_clue_sum = sum(row_definition)
        generated_rows = []

        for positions in combinations(range(row_size), number_clue_sum):
            p = [0] * row_size
            for i in positions:
                p[i] = 1
            generated_rows.append(p)

        return generated_rows

    @staticmethod
    def check_row_is_valid(row_definition, row):

        count = 0
        row_numbers = []
        for index in row:
            if index:
                count += 1
            elif count != 0:
                row_numbers.append(count)
                count = 0
        if count != 0:
            row_numbers.append(count)

        if row_numbers.__eq__(row_definition):
            return True
        else:
            return False

    def solve(self, nonogram_definition):
        row_definitions = nonogram_definition[0]
        col_definitions = nonogram_definition[1]
        col_size = len(row_definitions)
        row_size = len(row_definitions)

        count = 0
        for rowDefinition in row_definitions:
            count += 1
            possible_rows = self.generate_possible_rows(rowDefinition, row_size)

            possible_valid_rows = []
            for row in possible_rows:
                if self.check_row_is_valid(rowDefinition, row):
                    possible_valid_rows.append(row)

            print("Possible rows for row: " + str(count))
            print(possible_valid_rows)

        return True
