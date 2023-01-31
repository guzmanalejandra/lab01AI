
from PIL import Image
import numpy as np

def matrimage(image):

    image = Image.open(image)
    pixels = image.load()

    width, height = image.size
    width2 = int(width / 5)
    height2 = int(height / 5)

    color_matrix = [[0 for _ in range(width2)] for _ in range(height2)]

    red_like = 200
    green_like= 200

    for i in range(0, width, 5):
        for j in range(0, height, 5):
            r, g, b = pixels[i, j]

            if r == 0 and g == 0 and b == 0:
                color_matrix[int(i/5)][int(j/5)] = 0  # Black
            elif r == 255 and g == 255 and b == 255:
                color_matrix[int(i/5)][int(j/5)] = 1  # White
            elif r > red_like and g < red_like and b < red_like:
                color_matrix[int(i/5)][int(j/5)] = 2  # Red-like
            elif r < green_like and g > green_like and b < green_like:
                color_matrix[int(i/5)][int(j/5)] = 3  # Green-like


    return color_matrix