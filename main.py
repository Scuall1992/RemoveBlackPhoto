import os
from PIL import Image


for i in os.listdir("."):
    if ".jpg" in i:
        img = Image.open(i)
        img.thumbnail((100, 100))
        pixels = list(img.getdata())
        if len(set(["".join(map(str, i)) for i in pixels])) == 1:
            os.remove(i)
