from PIL import Image, ImageDraw

class img:

    def drawNonogram(self, nonogram):
        print(nonogram)
        rows = nonogram[0]
        columns = nonogram[1]
        height = len(rows)
        width = len(columns)
        gridSize = 14
        gridStartX, gridStartY = self.getGridStartCoordinates(columns, rows, gridSize)

        # Calculate image size and create image
        lengthX = ((gridSize * width) +1) + gridStartX
        lengthY = ((gridSize * height)+1) + gridStartY
        image = Image.new(mode='L', size=(lengthX, lengthY), color=255)

        # Draw Nonogram grid
        stepSize = int((image.height - gridStartY) / len(rows))
        self.drawHorizontalLines(image, gridStartY, stepSize)
        self.drawVerticalLines(image, gridStartX, stepSize)

        # Draw number clues
        self.drawHorizontalNumbers(image, gridStartX, gridStartY, stepSize, columns)
        self.drawVerticalNumbers(image, gridStartX, gridStartY, stepSize, rows)

        image.save('nonogram.bmp')

    def drawHorizontalNumbers(self, image, gridStartX, gridStartY, stepSize, columns):
        draw = ImageDraw.Draw(image)
        drawPosX = gridStartX + 3

        for column in columns:
            drawPosY = gridStartY - stepSize
            for numberClue in reversed(column):
                if numberClue >  9:
                    draw.text((drawPosX-2, drawPosY), str(numberClue))
                else:
                    draw.text((drawPosX, drawPosY), str(numberClue))
                drawPosY -= stepSize
            drawPosX += stepSize

    def drawVerticalNumbers(self, image, gridStartX, gridStartY, stepSize, rows):
        draw = ImageDraw.Draw(image)
        drawPosY = gridStartY
        for row in rows:
            drawPosX = gridStartX - stepSize
            for numberClue in reversed(row):
                draw.text((drawPosX, drawPosY), str(numberClue))
                drawPosX -= stepSize
            drawPosY += stepSize

    def getGridStartCoordinates(self, columns, rows, gridSize):

        maxColumnLength = 0
        for column in columns:
            if len(column) > maxColumnLength:
                maxColumnLength = len(column)
        gridStartY = maxColumnLength * gridSize

        maxRowLength = 0
        for row in rows:
            if len(row) > maxRowLength:
                maxRowLength = len(row)
        gridStartX = maxRowLength * gridSize

        return gridStartX, gridStartY

    def drawHorizontalLines(self, image, gridStartX, stepSize):
        draw = ImageDraw.Draw(image)

        for y in range(gridStartX, image.height, stepSize):
            line = ((0, y), (image.width, y))
            draw.line(line, fill=128)

    def drawVerticalLines(self, image, gridStartY, stepSize):
        draw = ImageDraw.Draw(image)

        for x in range(gridStartY, image.width, stepSize):
            line = ((x, 0), (x, image.height))
            draw.line(line, fill=128)