from PIL import Image, ImageDraw


class Img:

    def draw_nonogram(self, nonogram):
        rows = nonogram[0]
        columns = nonogram[1]
        height = len(rows)
        width = len(columns)
        grid_size = 16  # Magic number, makes good looking puzzles
        grid_start_x, grid_start_y = self.get_grid_start_coordinates(columns, rows, grid_size)

        # Calculate image size and create image
        length_x = ((grid_size * width) +1) + grid_start_x
        length_y = ((grid_size * height)+1) + grid_start_y
        image = Image.new(mode='L', size=(length_x, length_y), color=255)

        # Draw Nonogram grid
        step_size = int((image.height - grid_start_y) / len(rows))
        self.draw_horizontal_lines(image, grid_start_y, step_size)
        self.draw_vertical_lines(image, grid_start_x, step_size)

        # Draw number clues
        self.draw_horizontal_numbers(image, grid_start_x, grid_start_y, step_size, columns)
        self.draw_vertical_numbers(image, grid_start_x, grid_start_y, step_size, rows)

        image.save('nonogram.bmp')

    @staticmethod
    def draw_horizontal_numbers(image, grid_start_x, grid_start_y, step_size, columns):
        draw = ImageDraw.Draw(image)
        draw_pos_x = grid_start_x + 5

        for column in columns:
            draw_pos_y = (grid_start_y + 4)- step_size
            for numberClue in reversed(column):
                if numberClue > 9:
                    draw.text((draw_pos_x-2, draw_pos_y), str(numberClue))
                else:
                    draw.text((draw_pos_x, draw_pos_y), str(numberClue))
                draw_pos_y -= step_size
            draw_pos_x += step_size

    @staticmethod
    def draw_vertical_numbers(image, grid_start_x, grid_start_y, step_size, rows):
        draw = ImageDraw.Draw(image)
        draw_pos_y = grid_start_y
        for row in rows:
            draw_pos_x = (grid_start_x + 4) - step_size
            for numberClue in reversed(row):
                draw.text((draw_pos_x, draw_pos_y), str(numberClue))
                draw_pos_x -= step_size
            draw_pos_y += step_size

    @staticmethod
    def get_grid_start_coordinates(columns, rows, grid_size):

        max_column_length = 0
        for column in columns:
            if len(column) > max_column_length:
                max_column_length = len(column)
        grid_start_y = max_column_length * grid_size

        max_row_length = 0
        for row in rows:
            if len(row) > max_row_length:
                max_row_length = len(row)
        grid_start_x = max_row_length * grid_size

        return grid_start_x, grid_start_y

    @staticmethod
    def draw_horizontal_lines(image, grid_start_x, step_size):
        draw = ImageDraw.Draw(image)

        for y in range(grid_start_x, image.height, step_size):
            line = ((0, y), (image.width, y))
            draw.line(line, fill=128)

    @staticmethod
    def draw_vertical_lines(image, grid_start_y, step_size):
        draw = ImageDraw.Draw(image)

        for x in range(grid_start_y, image.width, step_size):
            line = ((x, 0), (x, image.height))
            draw.line(line, fill=128)