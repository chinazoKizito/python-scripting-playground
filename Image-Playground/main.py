from PIL import Image

# Bluring an image
img = Image.open('pokedex/pikachu.jpg')
new_img = img.convert('L')
new_img.save('blurpika.png', 'png')

# Converting an image to a thumbnail
img2 = Image.open('pokedex/charmander.jpg')
img2.thumbnail((120, 120))
img2.save('thumbcharmander.png', 'png')
