import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED


def view(file_name):
	layout = [
		[
			sg.Text(
				size=(2, 0),
				background_color='#282a36'
			),
			sg.Image(
				filename=f'./QRCodes/{file_name}.png',
				background_color='#282a36',
				size=(500, 500)
			)
		]
	]

	window = sg.Window(
   'QRCode Image', layout,
   background_color='#282a36',
   size=(500, 500),
   location=(540, 5))

	while True:
		events, values = window.read()
		if events == WIN_CLOSED:
			break
