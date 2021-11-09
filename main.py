import PySimpleGUI as sg
from generate import new_qr
from view_img import view

layout = [
	[
		sg.Text(
			'Digite aqui as informações:',
			background_color='#282a36', 
			text_color='#bd93f9', 
			font='"Fira Code" 12', 
			size=(75, 0)
		)
	],

	[
		sg.Multiline(
			font='"Fira Code" 12', 
			background_color='#44475a', 
			size=(35, 6), 
			key='info'
		)
	],

	[
		sg.Button(
			'Ok',
			font='"Fira Code" 12',
			button_color='#44475a'
		),
		sg.Text(
			size=(19, 0), 
			background_color='#282a36'
		),
		sg.Button(
			'Sair', 
			font='"Fira Code" 12', 
			button_color='#ff5555'
		),
	]
]

window = sg.Window(
  'QRCode Coverter',
  layout,
  background_color='#282a36',
  size=(300, 210),
  location=(450, 200)
)

while True:
	events, values = window.read()
	if events == sg.WIN_CLOSED or events == 'Sair':
		break

	if events == 'Ok':
		view(new_qr(values['info']))
