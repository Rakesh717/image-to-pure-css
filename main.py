import sys

from PIL import Image


def writeHeader(file):
    file.write('''<!DOCTYPE html>
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
    <body>''')


def writeFooter(file):
    file.write('''</body>
    </html>''')


def writeImage(file, height, width, pixels):
    file.write('<div class="image">')
    for i in range(height):
        file.write('<div style="display: flex">')
        for j in range(width):
            file.write(
                f'<div class="pixel" style="background-color: rgb({pixels[j,i][0]}, {pixels[j,i][1]}, {pixels[j,i][2]})"></div>'
            )
        file.write('</div>')

    file.write('</div>')


def convertImageToCss(filepath):
    img = Image.open(filepath)
    pixels = img.load()

    [width, height] = img.size

    with open('./index.html', 'w') as html:
        writeHeader(html)

        writeImage(html, height, width, pixels)

        writeFooter(html)


if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("File path is missing, try: python main.py ./test.jpeg")
    else:
        convertImageToCss(sys.argv[1])
