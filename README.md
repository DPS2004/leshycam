# Leshy's Camera
Generate Inscryption styled portrait sprites from any image.

# Setup and Config
This project uses PIL and ConfigParser.

The following values can be edited in config.ini:

images_in: The folder that Leshy's Camera uses as input

images_out: The folder that Leshy's Camera uses as input

palette: The number of colors per card. Set to 0 for a random palette each image.


# Notes on colors:
Most cards use either 2 brightness levels, 000 and 255

or 3 brightness levels, 000, 140, and 255

I'd guess that 90% of the cards use this.

Other level counts I found were:

4 (used for Alpha, Caged Wolf): 000, 100, 170, 255

5 (used for Amalgam, Lice): 000, 092, 127, 175, 255

Exceptions:

Greater Smoke, 8 colors: 000, 051, 70, 100, 127, 143, 191, 255

Undead Cat, 3 colors: 0, 51, FF0000 (red)