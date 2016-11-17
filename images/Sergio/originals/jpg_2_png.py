from PIL import Image
import re


find = re.compile(r'^[^0-9]*')

#Convert each image of names.txt from png to jpeg

with open('names.txt', 'r') as f:
    names = f.read().splitlines()

for name in names:

    img = Image.open(name)        
    
    img.save(name.split('.')[0] + '.png', 'png')
