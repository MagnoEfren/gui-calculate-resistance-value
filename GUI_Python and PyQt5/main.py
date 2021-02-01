import sys
from GUI import *


class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form() 
		self.ui.setupUi(self)

		self.multiplicadorDIC = {
		"Plata":0.01,
		"Oro":0.1,
		"Negro":1,
		"Marron":10,
		"Rojo":100,
		"Naranjado":1000,
		"Amarillo":10000,
		"Verde":100000,
		"Azul":1000000,
		"Violeta":10000000
		}

		self.colorDIC = {
		"Negro":0,
		"Marron":1,
		"Rojo":2,
		"Naranjado":3,
		"Amarillo":4,
		"Verde":5,
		"Azul":6,
		"Violeta":7,
		"Gris":8,
		"Blanco":9
		}


		self.toleracionDIC = {
		"Ninguna":20,
		"Plata":10,
		"Oro":5,
		"Rojo":2
		}
		self.valor1 = int(0)
		self.valor2 = int(0)
		self.valor3 = int(0)
		self.valor4 = int(0)
		self.Tol = int(0)

		self.ui.bt_resultado.clicked.connect(self.obtener_Resultado)

		self.ui.selec1.addItems(self.colorDIC.keys())
		self.ui.selec1.currentIndexChanged.connect(self.seleccion1)
		self.ui.selec1.setCurrentText("Negro")

		self.ui.selec2.addItems(self.colorDIC.keys())
		self.ui.selec2.currentIndexChanged.connect(self.seleccion2)
		self.ui.selec2.setCurrentText("Negro")

		self.ui.selec3.addItems(self.multiplicadorDIC.keys())
		self.ui.selec3.currentIndexChanged.connect(self.seleccion3)
		self.ui.selec3.setCurrentText("Negro")

		self.ui.selec4.addItems(self.toleracionDIC.keys())
		self.ui.selec4.currentIndexChanged.connect(self.seleccion4)
		self.ui.selec4.setCurrentText("Ninguno")


	def seleccion1(self):
		valor1 = self.ui.selec1.currentText()

		if valor1=="Negro":
			self.ui.label1.setStyleSheet("background-color: rgb(0, 0, 0)")
			valor1 = 0

		elif valor1 =="Marron":
			self.ui.label1.setStyleSheet("background-color: rgb(118, 51, 51)")
			self.valor1 = 1

		elif valor1 =="Rojo":
			self.ui.label1.setStyleSheet("background-color: rgb(255, 0, 0)")
			self.valor1 = 2

		elif valor1 =="Naranjado":
			self.ui.label1.setStyleSheet("background-color: rgb(255, 139, 3)")
			self.valor1 = 3

		elif valor1 =="Amarillo":
			self.ui.label1.setStyleSheet("background-color: rgb(251, 244, 11)")
			self.valor1 = 4

		elif valor1 =="Verde":
			self.ui.label1.setStyleSheet("background-color: rgb(0, 255, 0)")
			self.valor1 = 5

		elif valor1 =="Azul":
			self.ui.label1.setStyleSheet("background-color: rgb(0, 0, 255)")
			self.valor1 = 6

		elif valor1 =="Violeta":
			self.ui.label1.setStyleSheet("background-color: rgb(244, 11, 251)")
			self.valor1 = 7

		elif valor1 =="Gris":
			self.ui.label1.setStyleSheet("background-color: rgb(119, 119, 119)")
			self.valor1 = 8

		elif valor1 =="Blanco":
			self.ui.label1.setStyleSheet("background-color: rgb(0, 0, 0)")
			self.valor1 = 9


	def seleccion2(self):
		valor2 = self.ui.selec2.currentText()

		if valor2=="Negro":
			self.ui.label2.setStyleSheet("background-color: rgb(0, 0, 0)")
			self.valor2 = 0

		elif valor2 =="Marron":
			self.ui.label2.setStyleSheet("background-color: rgb(118, 51, 51)")
			self.valor2 = 1

		elif valor2 =="Rojo":
			self.ui.label2.setStyleSheet("background-color: rgb(255, 0, 0)")
			self.valor2 = 2

		elif valor2 =="Naranjado":
			self.ui.label2.setStyleSheet("background-color: rgb(255, 139, 3)")
			self.valor2 = 3

		elif valor2 =="Amarillo":
			self.ui.label2.setStyleSheet("background-color: rgb(251, 244, 11)")
			self.valor2 = 4

		elif valor2 =="Verde":
			self.ui.label2.setStyleSheet("background-color: rgb(0, 255, 0)")
			self.valor2 = 5

		elif valor2 =="Azul":
			self.ui.label2.setStyleSheet("background-color: rgb(0, 0, 255)")
			self.valor2 = 6

		elif valor2 =="Violeta":
			self.ui.label2.setStyleSheet("background-color: rgb(244, 11, 251)")
			self.valor2 = 7

		elif valor2 =="Gris":
			self.ui.label2.setStyleSheet("background-color: rgb(119, 119, 119)")
			self.valor2 = 8

		elif valor2 =="Blanco":
			self.ui.label2.setStyleSheet("background-color: rgb(0, 0, 0)")
			self.valor2 = 9

	def seleccion3(self):
		valor3 = self.ui.selec3.currentText()
		
		if valor3=="Plata":
			self.ui.label3.setStyleSheet("background-color: rgb(180, 180, 180)")
			self.valor3 = 0.01

		elif valor3 =="Oro":
			self.ui.label3.setStyleSheet("background-color: rgb(180, 130, 35)")
			self.valor3 = 0.1


		elif valor3=="Negro":
			self.ui.label3.setStyleSheet("background-color: rgb(0, 0, 0)")
			self.valor3 = 1

		elif valor3 =="Marron":
			self.ui.label3.setStyleSheet("background-color: rgb(118, 51, 51)")
			self.valor3 = 10

		elif valor3 =="Rojo":
			self.ui.label3.setStyleSheet("background-color: rgb(255, 0, 0)")
			self.valor3 = 100

		elif valor3 =="Naranjado":
			self.ui.label3.setStyleSheet("background-color: rgb(255, 139, 3)")
			self.valor3 = 1000

		elif valor3 =="Amarillo":
			self.ui.label3.setStyleSheet("background-color: rgb(251, 244, 11)")
			self.valor3 = 10000

		elif valor3 =="Verde":
			self.ui.label3.setStyleSheet("background-color: rgb(0, 255, 0)")
			self.valor3 = 100000

		elif valor3 =="Azul":
			self.ui.label3.setStyleSheet("background-color: rgb(0, 0, 255)")
			self.valor3 = 1000000

		elif valor3 =="Violeta":
			self.ui.label3.setStyleSheet("background-color: rgb(244, 11, 251)")
			self.valor3 = 10000000

	def seleccion4(self):
		valor4 = self.ui.selec4.currentText()
		
		if valor4=="Ninguna":
			self.ui.label4.setStyleSheet("background-color: rgb(245, 230, 255)")
			self.valor4 = 0.2
			self.Tol = "20%"

		elif valor4 =="Plata":
			self.ui.label4.setStyleSheet("background-color: rgb(180, 180, 180)")
			self.valor4 = 0.1
			self.Tol = "10%"

		elif valor4 =="Oro":
			self.ui.label4.setStyleSheet("background-color: rgb(188, 130, 35)")
			self.valor4 = 0.05
			self.Tol = "5%"

		elif valor4 =="Rojo":
			self.ui.label4.setStyleSheet("background-color: rgb(255, 0, 0)")
			self.valor4 = 0.02
			self.Tol = "2%"


	def obtener_Resultado(self):

		ValorG = str((self.valor1)) + str((self.valor2))
		X = float(self.valor3)
		Y = float(ValorG)
		
		ValorTT= float("{0:.3f}".format(X*Y))

		Vmax = ValorTT + (ValorTT*(float(self.valor4)))
		Vmin = ValorTT - (ValorTT*(float(self.valor4)))

		VmaxF = float("{0:.3f}".format(Vmax))
		VminF = float("{0:.3f}".format(Vmin))

		self.ui.resultado.setText(str(ValorTT))
		self.ui.tolerancia.setText(str(self.Tol))
		self.ui.maximo.setText(str(VmaxF))
		self.ui.minimo.setText(str(VminF))


		
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		
