from PIL import Image, ImageDraw

def pixelimage(image):

    im = Image.open(image)
    im = im.resize((140, 140))

    pixelated = Image.new('RGB', im.size, (255, 255, 255))
    pixels = im.load()

    matrix = [[0 for x in range(im.size[0])] for y in range(im.size[1])]

    for x in range(0, im.size[0], 5):
        for y in range(0, im.size[1], 5):
            pixel_color = pixels[x, y]

            colors = {}
            for i in range(x, x + 5):
                for j in range(y, y + 5):
                    try:
                        colors[pixels[i, j]] += 1
                    except KeyError:
                        colors[pixels[i, j]] = 1


            colors2 = {}

            for color in colors:
                if color[0] > 100 and color[1] < 50 and color[2] < 50:
                    try:
                        colors2[(255, 0, 0)] =+ colors[color]
                    except KeyError:
                        colors2[(255, 0, 0)] = colors[color]
                elif color[0] < 50 and color[1] > 100 and color[2] < 50:
                    try:
                        colors2[(0, 255, 0)] += colors[color]
                    except KeyError:
                        colors2[(0, 255, 0)] = colors[color]
                elif color[0] > 125 and color[1] > 125 and color[2] > 125:
                    try:
                        colors2[(255, 255, 255)] += colors[color]
                    except KeyError:
                        colors2[(255, 255, 255)] = colors[color]
                elif color[0] < 126 and color[1] < 126 and color[2] < 126:
                    try:
                        colors2[(0, 0, 0)] += colors[color]
                    except KeyError:
                        colors2[(0, 0, 0)] = colors[color]

            white = colors2[(255, 255, 255)] if (255, 255, 255) in colors2 else 0
            black = colors2[(0, 0, 0)] if (0, 0, 0) in colors2 else 0

            if white > black:
                pixel_color = (255, 255, 255)
            else:
                pixel_color = (0, 0, 0)


            if (255, 0, 0) in colors2 and colors2[(255, 0, 0)] >= 1:
                pixel_color = (255, 0, 0)
            
            if (0, 255, 0) in colors2 and colors2[(0, 255, 0)] >= 3:
                pixel_color = (0, 255, 0)

            if pixel_color == (255, 0, 0) or pixel_color == (0, 255, 0):
                try:
                    if matrix[x+5][y] == pixel_color or matrix[x+10][y] == pixel_color:
                        pixel_color = (255, 255, 255)
                except IndexError:
                    pass

                try:
                    if matrix[x-5][y] == pixel_color or matrix[x-10][y] == pixel_color:
                        pixel_color = (255, 255, 255)
                except IndexError:
                    pass

                try:
                    if matrix[x][y+5] == pixel_color or matrix[x][y+10] == pixel_color:
                        pixel_color = (255, 255, 255)
                except IndexError:
                    pass

                try:
                    if matrix[x][y-5] == pixel_color or matrix[x][y-10] == pixel_color:
                        pixel_color = (255, 255, 255)
                except IndexError:
                    pass

                try:
                    if matrix[x+5][y+5] == pixel_color or matrix[x+10][y+10] == pixel_color or matrix[x+5][y+10] == pixel_color or matrix[x+10][y+5] == pixel_color:
                        pixel_color = (255, 255, 255)
                except IndexError:
                    pass

                try:
                    if matrix[x-5][y-5] == pixel_color or matrix[x-10][y-10] == pixel_color or matrix[x-5][y-10] == pixel_color or matrix[x-10][y-5] == pixel_color:
                        pixel_color = (255, 255, 255)
                except IndexError:
                    pass

                try:
                    if matrix[x+5][y-5] == pixel_color or matrix[x+10][y-10] == pixel_color or matrix[x+5][y-10] == pixel_color or matrix[x+10][y-5] == pixel_color:
                        pixel_color = (255, 255, 255)
                except IndexError:
                    pass

                try:
                    if matrix[x-5][y+5] == pixel_color or matrix[x-10][y+10] == pixel_color or matrix[x-5][y+10] == pixel_color or matrix[x-10][y+5] == pixel_color:
                        pixel_color = (255, 255, 255)
                except IndexError:
                    pass

            #save pixel_color to matrix
            for i in range(x, x + 5):
                for j in range(y, y + 5):
                    matrix[i][j] = pixel_color
            
            ImageDraw.Draw(pixelated).rectangle([(x, y), (x + 5, y + 5)], fill=pixel_color)

    pixelated.save('mazes/renderizada.bmp')