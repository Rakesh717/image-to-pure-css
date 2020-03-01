from PIL import Image

header = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image</title>
    <style>
        .pixel{
            height: 1px;
            width: 1px;
        }


    </style>
</head>
<body>'''

footer = '''</body>
</html>'''

img = Image.open('/home/rakesh/Pictures/Wallpapers/rakesh.jpg')
pix = img.load()  # gets the pixel of image

width = img.size[0]
height = img.size[1]

with open('/home/rakesh/image.html', 'w') as html:
    html.write(header)
    html.write(
        f'<div class="image" style="height: {height}px; width: {width}px">')
    for i in range(height):
        html.write('<div style="display: flex">')
        for j in range(width):
            html.write(
                f'<div class="pixel" style="background-color: rgb({pix[j,i][0]}, {pix[j,i][1]}, {pix[j,i][2]})"></div>'
            )
        html.write('</div>')
    
    html.write(footer)
