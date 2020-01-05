from PIL import Image

a = Image.open("./myp-design/cozmo/assets/cozmo-screen-code.png")
b = Image.open("./myp-design/cozmo/assets/cozmo-connection.png")
c = Image.open("./myp-design/cozmo/assets/qr-video-connection.png")
print(a.width, a.height, b.width, b.height, c.width, c.height)
b = b.resize((a.width, int(a.width*b.height/b.width)))
c = c.resize((a.width, int(a.width*c.height/c.width)))
d = Image.new("RGB", (530, a.height+b.height+c.height))
d.paste(a, (0,0))
d.paste(b, (0, a.height))
d.paste(c, (0, a.height+b.height))
d.save("./myp-design/cozmo/assets/cozmo-connection2.png")
d.show()
