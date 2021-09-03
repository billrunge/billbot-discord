import os
import numpy as np
import urllib3
import io
from distutils.util import strtobool
from PIL import Image

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^'. "
gscale2 = '@%#*+=-:. '
 
def getAverageL(image):
    im = np.array(image) 
    w,h = im.shape
    return np.average(im.reshape(w*h))
 
async def covertImageToAscii(fileUrl, cols, scale, moreLevels):
    global gscale1, gscale2

    pool = urllib3.PoolManager()
    resp = pool.request('GET', fileUrl)
    data = io.BytesIO(resp.data)
    image = Image.open(data).convert('L')
 
    W, H = image.size[0], image.size[1]
 
    w = W/cols
    h = w/scale
    rows = int(H/h)

    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    aimg = []

    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
 
        if j == rows-1:
            y2 = H
 
        aimg.append("")
 
        for i in range(cols):
 
            x1 = int(i*w)
            x2 = int((i+1)*w)
 
            if i == cols-1:
                x2 = W
 
            img = image.crop((x1, y1, x2, y2))
 
            avg = int(getAverageL(img))

            if moreLevels:
                gsval = gscale1[int((avg*68)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
 
            aimg[j] += gsval

    return aimg

async def messageToAscii(message):
    if len(message.attachments) > 0:
        for attachment in message.attachments:
            aimg = await covertImageToAscii(attachment.url, 40, 0.43, True)
            ascii_image = ''
            for row in aimg:
                ascii_image += f'`{row}`\n'
        await message.channel.send(ascii_image)

async def execute(message):    
    if bool(strtobool(os.getenv('CHANNEL_LIMITED'))) and str(message.channel.id) == os.getenv('CHANNEL_ID'):
        await messageToAscii(message)        
    elif not bool(strtobool(os.getenv('CHANNEL_LIMITED'))):
        await messageToAscii(message)
        
