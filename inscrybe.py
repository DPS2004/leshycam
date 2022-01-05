import sys
import os
from PIL import Image

# adapted from https://stackoverflow.com/a/29438149
def quantizetopalette(silf, palette, dither=False):
    """Convert an RGB or L mode image to use a given P image's palette."""

    silf.load()

    palette.load()
    if palette.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
            )
    im = silf.im.convert("P", 1 if dither else 0, palette.im)

    try:
        return silf._new(im)
    except AttributeError:
        return silf._makeself(im)
def makepaletteimage(palettedata):

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

basepath = "cards/"

# NOTES ON COLORS:
# Most cards use 3 colors, 000,127,and 255.
# I'd guess that 90% of the cards use this.
# The other most common color count i found was five, used on cards like Amalgam.
# inscryption uses 5 colors, including black and white.

makepaletteimage([0,0,0,

print("loading images...")
images = []
for imgfn in os.listdir(basepath):
    print(imgfn)

    ogimg = Image.open(basepath + imgfn)
    
    

    ogimg.save("out.png")    
    break
print("done!")


