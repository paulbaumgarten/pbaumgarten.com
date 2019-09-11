# Python Pillow

Pillow is the Python library for image manipulation.

## Install

```bash
sudo pip3 install pillow
```

## Example code snippets

Resizing an image

```python
from PIL import Image

def resize(source_filename, dest_filename, new_height):
    im = Image.open(source_filename)
    new_width = round(im.width * new_height / im.height)
    out = im.resize((new_width, new_height))
    out.save(dest_filename)
```

## Background colour removal

```python
from PIL import Image
from PIL import ImageFilter

def hex_to_rgb(value):
    """ Converts `#ffffff` to (255,255,255) """
    value = value.lstrip('#')
    r = int(value[:2], 16)
    g = int(value[2:4], 16)
    b = int(value[4:], 16)
    return (r,g,b)

def image_remove_background( source_filename, target_filename, background_color="#ffffff", sensitivity=25):
    """ sensitivity is out of 256 """
    img = Image.open(source_filename)  
    img = img.convert("RGBA")  
    remove_color = hex_to_rgb(background_color)
    pixdata = img.load()  
    for y in range(img.size[1]):  
        for x in range(img.size[0]):  
                r, g, b, a = img.getpixel((x, y))  
                if abs(remove_color[0]-r)<sensitivity and abs(remove_color[1]-g)<sensitivity and abs(remove_color[2]-b)<sensitivity:
                    pixdata[x, y] = (0, 0, 0, 0)  # make it transparent
    img2 = img.filter(ImageFilter.GaussianBlur(radius=1))  
    if target_filename[-4:].lower() in (".jpg", ".jpe"):
        target_filename = target_filename[:-4] + ".png"
    img2.save(target_filename, "PNG")  
```

## Conversions

```python
def convert_pil_to_numpy( pil_image ):
    from PIL import Image
    import numpy as np
    im2arr = np.array(im)     # note: im2arr.shape will return height x width x channel
    return im2arr

def convert_numpy_to_pil( np_image ):
    from PIL import Image
    import numpy as np
    arr2im = Image.fromarray(im2arr)
    return arr2im

def convert_cv2_to_pil( cv2_image ):
    import cv2
    from PIL import Image
    cv2_image_rgb = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cv2_image_rgb)
    return pil_image

def convert_pil_to_cv2( pil_image ):
    import cv2
    import numpy as np
    from PIL import Image
    cv2_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return cv2_image

```

## Reference

* [Python Imaging Librar Overview](/python/pillow-handbook.pdf) 77 page PDF for PIL 1.1.3, March 12, 2002 by Fredrik Lundh, Matthew Ellis
* [Pillow (Python Imaging Library) documentation](https://pillow.readthedocs.io/en/stable/)
* [Open CV documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

