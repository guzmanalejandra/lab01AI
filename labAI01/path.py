from PIL import Image

def pathlineart(file, shortest_path):
    image = Image.open(file)
    path_image = image.copy()
    pixels = path_image.load()

    path_color = (128, 0, 128)
    for i, j in shortest_path:
        for x in range(i*5, (i*5) + 5):
            for y in range((j*5), (j*5) + 5):

                #check if current position is not red or green
                if pixels[x, y] != (255, 0, 0) and pixels[x, y] != (0, 255, 0):
                    pixels[x, y] = path_color

    path_image.save("result.jpg")
