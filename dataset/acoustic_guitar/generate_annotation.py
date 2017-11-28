from PIL import Image
from os import listdir
from os.path import isfile, join

path = '.'
files = [f for f in listdir(path) if isfile(join(path, f))]

# print files

f = open('dimensions', 'w')

for file in files:
	if(file.endswith('.jpeg') or file.endswith('.JPEG')):
		with Image.open(file) as img:
			width, height = img.size
			dimensions = file + " " + str(width) + " " + str(height) + "\n"
			f.write(dimensions)