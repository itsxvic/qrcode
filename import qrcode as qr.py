import qrcode as qr

data = "https://github.com/itsxvic"

img = qr.make (data)
img.save ('C:/Users/casti_ivip3np/OneDrive/Área de Trabalho/projetoqrcode.py/myqrcode.png')

data = "https://www.instagram.com/itsxvic/"

img = qr.make (data)
img.save ('C:/Users/casti_ivip3np/OneDrive/Área de Trabalho/projetoqrcode.py/myqrcode1.png')