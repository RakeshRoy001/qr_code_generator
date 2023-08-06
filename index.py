import qrcode
generate_image = qrcode.make("https://github.com/RakeshRoy001")
generate_image.save('image1.png')