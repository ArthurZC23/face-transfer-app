from PIL import Image
import re


find = re.compile(r'^[^0-9]*')

#Convert each image of names.txt from png to jpeg

with open('names.txt', 'r') as f:
    names = f.read().splitlines()

for name in names:
    
    number = int(re.findall(r'\d+', name)[0])
    
    number /= 5
    
    img = Image.open(name)
    
    new_name = re.search(find, name).group(0)
    
    img.save(new_name + str(number) + '.png', 'png')
