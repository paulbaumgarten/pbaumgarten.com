from PIL import Image

a = Image.open("./myp-design/cozmo/assets/cozmo-screen-code.png")
b = Image.open("./myp-design/cozmo/assets/cozmo-connection.png")
b = b.resize((530, int(120*530/308)))
c = Image.new("RGB", (530, 645+206))
c.paste(a, (0,0))
c.paste(b, (0, 645))
c.save("./myp-design/cozmo/assets/cozmo-connection2.png")
c.show()
print(a.width, a.height, b.width, b.height)
