from PIL import Image

img = Image.new('RGB', (256, 256*2))
img1 = Image.open('out.jpg')
img2 = Image.open('out.jpg')

img.paste(img1, (0, 0))
img.paste(img2, (0, 256))
 
img.show()
img.save("result_merge.jpg")
