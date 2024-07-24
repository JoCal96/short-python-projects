import imageio.v3 as iio

filenames = ['gif_image_1.png', 'gif_image_2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('cartoon.gif', images, duration = 500, loop = 0)
