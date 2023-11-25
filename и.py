from PyQt5.QtWidgets import*


app=QApplication([])
window= QWidget()
window.resize(500,500)

a= QLabel("bananchiki")
numbera = QLabel("Номер переможця")
startBtn = QPushButton("ДІЗНАТИСЯ ПЕРЕМОЖЦЯ")

main_line  =  QHBoxLayout()
main_line.addWidget(a)
main_line.addWidget(numbera)
main_line.addWidget(startBtn)

window.setLayout(main_line)

def banana():
    a=random.randint(1,10)
    numbera.setText(str(a))
startBtn.clicked.connect(banana)
window.show()

app.exec()

