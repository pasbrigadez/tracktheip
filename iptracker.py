#!/usr/bin/env python
# Made in Bandung ( PasbrigadeZ ) with API https://ipapi.co
# I hope you can respect my work, by not removing this copyright
# Free to recode

import requests
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
	def __init__(self):
		super(Form, self).__init__()

		garis1 = QLabel('+'*75)

		gbr = QLabel()
		gbr.setPixmap(QPixmap('oray.png'))
		gbr.setAlignment(Qt.AlignCenter)

		garis2 = QLabel('+'*75)

		lbl = QLabel('IP You Wanna Track : ')

		garis3 = QLabel('+'*75)

		garis4 = QLabel('+'*75)

		regekkuh = QRegExp("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
		validator = QRegExpValidator(regekkuh)
		self.aypi = QLineEdit()
		self.aypi.setValidator(validator)
		self.aypi.setFixedWidth(125)
		self.aypi.setAlignment(Qt.AlignLeft)


		self.output = QLabel()
		self.output.setText("Negara : \nKota : \nWilayah : \nLokasi : \n")
		self.output.setFixedHeight(80)

		layouth = QHBoxLayout()
		layouth.addWidget(lbl)
		layouth.addWidget(self.aypi)
		layouth.addStretch()

		layoutv = QVBoxLayout()
		layoutv.addWidget(garis1)
		layoutv.addWidget(gbr)
		layoutv.addWidget(garis2)
		layoutv.addLayout(layouth)
		layoutv.addWidget(garis3)
		layoutv.addWidget(self.output)
		layoutv.addWidget(garis4)

		self.output.setTextInteractionFlags(Qt.TextSelectableByMouse)

		self.connect(self.aypi, SIGNAL("returnPressed(void)"), self.diklik)
		self.setLayout(layoutv)
		self.setWindowTitle('IP Tracker')
	def diklik(self):
		r = requests.get('https://ipapi.co/%s/json'%str(self.aypi.text()))
		owtput = "Negara : %s"%(r.json()['country_name'])+"\nKota : %s"%(r.json()['city']+"\nWilayah : %s"%(r.json()['region'])+"\nLokasi : https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&size=464x250&zoom=15"%(r.json()['latitude'],r.json()['longitude']))
		self.output.setText(owtput)

def main():
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	sys.exit(app.exec_())
if __name__=='__main__':
	main()
