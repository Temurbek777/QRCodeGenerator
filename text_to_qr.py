import qrcode


def text_to_qr(text):
    qr = qrcode.make(text)
    qr.save('qr.jpg')
    photo = open('qr.jpg', 'rb')
    return photo
