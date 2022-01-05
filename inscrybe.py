import sys
import os
from PIL import Image
import random
import configparser
import numpy as np

config = configparser.ConfigParser()
config.read('config.ini')

conf = config['main']

# adapted from https://stackoverflow.com/a/29438149
def quantizetopalette(silf, pal, dither=False):
    """Convert an RGB or L mode image to use a given P image's palette."""

    silf.load()

    pal.load()
    if pal.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
            )
    silf = silf.quantize(colors=256,palette=pal,dither=Image.NONE)
    return silf
def makepaletteimage(cpal):
    palettedata = cpal.copy()
    for x in range(0,len(palettedata)):
        col = palettedata[x*3]
        for i in range(0,2):
            palettedata.insert(x*3+i,col)
            
    
    NUM_ENTRIES_IN_PILLOW_PALETTE = 256
    num_bands = len("RGB")
    num_entries_in_palettedata = len(palettedata) // num_bands
    palettedata.extend(palettedata[:num_bands]
                       * (NUM_ENTRIES_IN_PILLOW_PALETTE
                          - num_entries_in_palettedata))
    # Create a palette image whose size does not matter
    arbitrary_size = 16, 16
    palimage = Image.new('P', arbitrary_size)
    palimage.putpalette(palettedata)
    return palimage
    

inpath = conf['images_in']
outpath = conf['images_out']
cpalind = int(conf['defaultpalette'])

imgsize = (int(conf['imagewidth']),int(conf['imageheight']))
finalsize = (int(conf['imagewidth'])*int(conf['imagescale']),int(conf['imageheight']*int(conf['imagescale'])))

palettes = {
    2: [0,255],
    3: [0,140,255],
    4: [0,100,170,255],
    5: [0,97,127,175,255],
    8: [0,51,70,100,127,143,191,255]
}

randpal = False

if cpalind == 0:
    randpal = True
    cpalind = 2

cpal = palettes[cpalind]
palimg = makepaletteimage(cpal)



try: 
    os.mkdir(outpath) 
    print("loading images...")
except:
    print("loading images...")
    # wow cool coding practices nice job
images = []
for imgfn in os.listdir(inpath):
    print('Photographing ' + imgfn)
    if randpal:
        cpalind = random.randint(2,5)
        cpal = palettes[cpalind]
        palimg = makepaletteimage(cpal)
    # Step 1: Open image!
    img = Image.open(inpath + imgfn)
    img = img.convert("RGB")
    
    # Step 2: quantize to the palette
    img = quantizetopalette(img,palimg)
    
    # Step 3: resize to desired resolution
    img = img.resize(imgsize,Image.NEAREST)
    
    # Step 4: Scale up and save
    
    img = img.resize(finalsize,Image.NEAREST)
    
    if conf.getboolean('transparent'):
        img = img.convert("RGBA")
        imarr = np.array(img)
        r,g,b,a = imarr.T
        for x in cpal:
            replacearea = (r == x)
            imarr[..., :][replacearea.T] = (0,0,0,255-x)
        img = Image.fromarray(imarr)
            
        
    
    img.save(outpath + imgfn)
print("done!")


