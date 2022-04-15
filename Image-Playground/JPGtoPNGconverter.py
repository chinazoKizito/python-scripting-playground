import sys
import os
from PIL import Image

original_folder = sys.argv[1]
new_folder = sys.argv[2]

print(original_folder, new_folder)

if not os.path.exists(new_folder):
    os.mkdir(new_folder)

for filename in os.listdir(original_folder):
    img = Image.open(f"{original_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done')