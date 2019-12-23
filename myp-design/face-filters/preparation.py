
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from PIL import ImageFont
import ImageTools
import time

# 1. Use camera to take photos, open photos from disk, save photos to disk

def task1a():
    camera = ImageTools.Camera()
    for _ in range(10):
        img = camera.take_photo()
        img.save("camera.png", "png")
        img.show()
        time.sleep(1)

def task1b():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    img.show()

# 2. Photo manipulation: Crop, resize, rotate, photo in photo

def task2a(): # draw a grid
    img = Image.open("./myp-design/face-filters/test-pic.png")
    width, height = img.size
    print(f"Image size is {width} x {height} pixels")
    draw = ImageDraw.Draw(img) # Create a drawing object linked to our image
    font = ImageFont.truetype("./myp-design/face-filters/assets/Roboto-Light.ttf", 16)
    for x in range(width):
        if x % 50 == 0:
            draw.line((x,0,x,height), fill=255, width=1)
            draw.text((x,0),str(x),(255,255,255),font=font)
    for y in range(height):
        if y % 50 == 0:
            draw.line((0,y,width,y), fill=255, width=1)
            draw.text((0,y),str(y),(255,255,255),font=font)
    img.show()

def task2b(): # crop it, resize it, rotate it
    # Open
    img = Image.open("./myp-design/face-filters/test-pic.png")
    # Crop
    img2 = img.crop((550,100,850,600)) # left, top, right, bottom
    # Resize
    width, height = img2.size
    new_width = int(width/3)
    new_height = int(height/3)
    img3 = img2.resize((new_width, new_height))
    # Rotate
    img4 = img3.rotate(90, fillcolor=(0,0,0)) # degrees anti-clockwise
    img5 = img3.rotate(90, expand=True, fillcolor=(0,0,0))
    # Display
    img4.show()
    img5.show()

def print_info(img):
    width, height = img.size
    mode = img.mode
    print(f"Image info: Size {img.size[0]} x {img.size[1]}, colour mode {mode}")

def task2c(): # photo in photo
    # Open
    img = Image.open("./myp-design/face-filters/test-pic.png")
    # Crop
    img2 = img.crop((550,100,850,600)).resize((100,166))
    img.paste(img2, (100,100))
    img.show()
    print_info(img)

"""
https://pillow.readthedocs.io/en/5.1.x/handbook/concepts.html

The following modes are available:
* `1` (1-bit pixels, black and white, stored with one pixel per byte)
* `L` (8-bit pixels, black and white)
* `P` (8-bit pixels, mapped to any other mode using a color palette)
* `RGB` (3x8-bit pixels, true color)
* `RGBA` (4x8-bit pixels, true color with transparency mask)
* `CMYK` (4x8-bit pixels, color separation)
* `YCbCr` (3x8-bit pixels, color video format) (this is the JPEG not the ITU-R BT.2020 standard)
* `LAB` (3x8-bit pixels, the L*a*b color space)
* `HSV` (3x8-bit pixels, Hue, Saturation, Value color space)
* `I` (32-bit signed integer pixels)
* `F` (32-bit floating point pixels)
"""


# 3. Simple filters: Black and white, re-colour, blur

def task3a():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    print_info(img)
    bw = img.convert(mode="1") # black and white
    grey = img.convert(mode="L") # greyscale
    bw.show()
    grey.show()

def task3b():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    img = img.crop((550,100,850,600)).resize((100,166))
    for y in range(0, img.height):
        for x in range(0, img.width):
            px = img.getpixel((x,y))
            print(f"{x},{y}={px}")
    print_info(img)
    # img.putpixel((x,y), color_tuple )

def task3c():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    img = img.crop((550,100,850,600)).resize((100,166))
    compiled = Image.new("RGBA", (700,166))
    blur = img.filter(ImageFilter.BLUR)
    blur.show()
    contour = img.filter(ImageFilter.CONTOUR)
    contour.show()
    detail = img.filter(ImageFilter.DETAIL)
    detail.show()
    edges = img.filter(ImageFilter.EDGE_ENHANCE)
    edges.show()
    emboss = img.filter(ImageFilter.EMBOSS)
    emboss.show()
    sharpen = img.filter(ImageFilter.SHARPEN)
    sharpen.show()
    smooth = img.filter(ImageFilter.SMOOTH)
    smooth.show()
    compiled.paste(blur, (0,0))
    compiled.paste(contour, (100,0))
    compiled.paste(detail, (200,0))
    compiled.paste(edges, (300,0))
    compiled.paste(emboss, (400,0))
    compiled.paste(sharpen, (500,0))
    compiled.paste(smooth, (600,0))
    draw = ImageDraw.Draw(compiled) # Create a drawing object linked to our image
    font = ImageFont.truetype("./myp-design/face-filters/assets/Roboto-Light.ttf", 16)
    draw.text((0,150),"Blur",(255,255,255),font=font)
    draw.text((100,150),"Contour",(255,255,255),font=font)
    draw.text((200,150),"Detail",(255,255,255),font=font)
    draw.text((300,150),"Edges",(255,255,255),font=font)
    draw.text((400,150),"Emboss",(255,255,255),font=font)
    draw.text((500,150),"Sharpen",(255,255,255),font=font)
    draw.text((600,150),"Smooth",(255,255,255),font=font)
    compiled.show()

def task3d():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    img = img.crop((550,100,850,600)).resize((100,166))
    compiled = Image.new("RGBA", (800,166))

    sharpness = ImageEnhance.Sharpness(img)
    img1 = sharpness.enhance(0.5) # decrease sharpness
    img2 = sharpness.enhance(1.5) # increase sharpness
    brightness = ImageEnhance.Brightness(img)
    img3 = brightness.enhance(0.5)
    img4 = brightness.enhance(1.5)
    contrast = ImageEnhance.Contrast(img)
    img5 = contrast.enhance(0.5)
    img6 = contrast.enhance(1.5)
    c = ImageEnhance.Color(img)
    img7 = c.enhance(0.5)
    img8 = c.enhance(1.5)
    img1.show()
    img2.show()
    img3.show()
    img4.show()
    img5.show()
    img6.show()
    img7.show()
    img8.show()

    compiled.paste(img1, (0,0))
    compiled.paste(img2, (100,0))
    compiled.paste(img3, (200,0))
    compiled.paste(img4, (300,0))
    compiled.paste(img5, (400,0))
    compiled.paste(img6, (500,0))
    compiled.paste(img7, (600,0))
    compiled.paste(img8, (700,0))
    draw = ImageDraw.Draw(compiled) # Create a drawing object linked to our image
    font = ImageFont.truetype("./myp-design/face-filters/assets/Roboto-Light.ttf", 16)
    draw.text((0,150),"Sharpness",(255,255,255),font=font)
    draw.text((200,150),"Brightness",(255,255,255),font=font)
    draw.text((400,150),"Contrast",(255,255,255),font=font)
    draw.text((600,150),"Color",(255,255,255),font=font)
    compiled.show()

def task3e():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    img = img.crop((550,100,850,600)).resize((100,166))
    img = img.convert("RGB")
    img = img.convert("RGB", matrix=(0.0,1.0,0.0,0.0, 1.0,0.0,0.0,0.0, 0.0,0.0,0.5,0.0))
    img = img.convert("RGBA")
    img.show()
    if isinstance(img, Image.Image):
        print("yes")
    else:
        print("no")

def task4a():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    faces_coordinates = ImageTools.get_faces(img, "./myp-design/face-filters/assets/haarcascade_frontalface_default.xml")
    if len(faces_coordinates) > 0:
        print("Faces found at the following locations")
        for face_location in faces_coordinates:
            print(face_location)
            x,y,w,h = face_location
            face_image = img.crop((x,y,x+w,y+h))
            face_image.show()

def task4b():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    draw = ImageDraw.Draw(img)
    faces_coordinates = ImageTools.get_faces(img, "./myp-design/face-filters/assets/haarcascade_frontalface_default.xml")
    if len(faces_coordinates) > 0:
        print("Faces found at the following locations")
        for face_location in faces_coordinates:
            x,y,w,h = face_location
            draw.rectangle((x,y,x+w,y+h), outline="#ffff00", width=5)
    img.show()

def task4c():
    img = Image.open("./myp-design/face-filters/test-pic.png")
    face_filter = Image.open("./myp-design/face-filters/filters/demo.png")
    draw = ImageDraw.Draw(img)
    faces_coordinates = ImageTools.get_faces(img, "./myp-design/face-filters/assets/haarcascade_frontalface_default.xml")
    if len(faces_coordinates) > 0:
        print("Faces found at the following locations")
        for face_location in faces_coordinates:
            print(face_location)
            x,y,w,h = face_location
            draw.rectangle((x,y,x+w,y+h), outline="#ffff00", width=5)
            adjusted_face_filter = face_filter.resize((h,w))
            img.paste(adjusted_face_filter, (x,y))
    img.show()

#task4c()

im = Image.open("/users/pbaumgarten/desktop/orig.jpg")
altered = im.crop((0,100,3000,2100))
print_info(altered)
im.save("my picture.png", "png")

img = Image.open("./myp-design/face-filters/test-pic.png")
img = Image.open("/users/pbaumgarten/desktop/faces.jpg")
faces_coordinates = ImageTools.get_faces(img, "./myp-design/face-filters/assets/haarcascade_frontalface_default.xml")
print(faces_coordinates)

# 4. OpenCV: Detect faces, bodies, face features
# 5. Complete the face filter demo


