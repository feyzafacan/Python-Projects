
import qrcode
import image

qr = qrcode.QRCode(
    version = 10, #15 means the version of the qr code high the number bigger the code image and complicated picture.
    box_size = 10,  #size of the box
    border = 5 # white part of the image -- border in all 4 sides with white color
)

# path for the qr. if you want to show a text in your qr code just write a text instead of link
data = "https://www.youtube.com/watch?v=D4BVkDwhea8 "


qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("qr_code.png")