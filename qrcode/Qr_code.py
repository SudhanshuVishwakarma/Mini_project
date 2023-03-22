import qrcode as qr

img = qr.make("https://ibb.co/j52YdQH")
img.save("genrated_qrcode.png")
