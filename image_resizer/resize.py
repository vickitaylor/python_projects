# install and import pillow
from PIL import Image

# open up the image you want to resize
# img = Image.open('test.png')

# print the current image size
# print(f"Current size: {img.size}")

# specify the size to change it to
# resize_image = img.resize((500, 500))

# save resized image
# resize_image.save('image_resized.jpg')

# way to let the user decided what to resize the image to

def resize_image(side1, side2):
    img = Image.open('test.png')
    print(f"Current size: {img.size}")

    resize_image = img.resize((side1, side2))

    resize_image.save(f'image{side1}.jpg')


size1 = int(input('Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(size1, size2)
