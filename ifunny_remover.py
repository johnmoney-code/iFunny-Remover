from PIL import Image
import glob, os

for infile in glob.glob('*.jpg'):
    name, ext = os.path.splitext(infile)
    input = Image.open(infile)
    width, height = input.size
    
    output = input.crop((0, 0, width, (height - 20)))

    if not os.path.exists('output'):
        os.makedirs('output')
    output.save('output\\' + name + '.jpg')
