import png, pyqrcode
from time import ctime

def new_qr(info):
	# values = info.replace('\\', '\n')
	name_file = ctime()
	qr = pyqrcode.create(info)
	qr.png(f'./QRCodes/{name_file}.png', scale=6)

	return name_file
