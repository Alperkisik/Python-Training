import sys
import random

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from tictactoeForm import Ui_MainWindow

class xoxGame(QtWidgets.QMainWindow):
    def __init__(self):
        super(xoxGame,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText('player') 
        self.ui.label_2.setText('0')
        self.ui.lbl_ai.setText('0')
        self.ui.lbl_player.setText('0')

        self.ui.btn1.clicked.connect(self.click)
        self.ui.btn2.clicked.connect(self.click)
        self.ui.btn3.clicked.connect(self.click)
        self.ui.btn4.clicked.connect(self.click)
        self.ui.btn5.clicked.connect(self.click)
        self.ui.btn6.clicked.connect(self.click)
        self.ui.btn7.clicked.connect(self.click)
        self.ui.btn8.clicked.connect(self.click)
        self.ui.btn9.clicked.connect(self.click)

        self.ui.btn_exit.clicked.connect(self.click_exit)

    def click(self):
        btn = self.sender()
        x = btn.text()
        t = int(self.ui.label_2.text())
        turn = self.ui.label.text()
        if x == '':
            if turn == 'player':
                btn.setText('X')
                turn = 'ai'
            else:
                btn.setText('O')
                turn = 'player'
            t = t + 1
            self.ui.label_2.setText(str(t))
            btn.setEnabled(False)
            
            buttons = self.ui.groupBox_2.findChildren(QtWidgets.QPushButton)
            moves = ['','','','','','','','','']            
            i = 0
            for b in buttons:
                moves[i] = b.text()
                print(str(i) + ' ' + str(moves[i]))
                i = i + 1  
            
            text =''
            if (moves[0] == moves[1]) & (moves[0] == moves[2]) & (moves[0] != ''):
                if moves[0] == 'X':
                    text = 'player wins'
                elif moves[0] == 'O':
                    text = 'ai wins'
            elif(moves[0] == moves[3]) & (moves[0] == moves[6]) & (moves[0] != ''):
                if moves[0] == 'X':
                    text = 'player wins'
                elif moves[0] == 'O':
                    text = 'ai wins'
            elif(moves[0] == moves[4]) & (moves[0] == moves[8]) & (moves[0] != ''):
                if moves[0] == 'X':
                    text = 'player wins'
                elif moves[0] == 'O':
                    text = 'ai wins'
            elif(moves[3] == moves[4]) & (moves[3] == moves[5]) & (moves[3] != ''):
                if moves[3] == 'X':
                    text = 'player wins'
                elif moves[3] == 'O':
                    text = 'ai wins'
            elif(moves[6] == moves[7]) & (moves[6] == moves[8]) & (moves[6] != ''):
                if moves[6] == 'X':
                    text = 'player wins'
                elif moves[6] == 'O':
                    text = 'ai wins'
            elif(moves[1] == moves[4]) & (moves[1] == moves[7]) & (moves[1] != ''):
                if moves[1] == 'X':
                    text = 'player wins'
                elif moves[1] == 'O':
                    text = 'ai wins'
            elif(moves[2] == moves[5]) & (moves[2] == moves[8]) & (moves[2] != ''):
                if moves[2] == 'X':
                    text = 'player wins'
                elif moves[2] == 'O':
                    text = 'ai wins'
            elif(moves[2] == moves[4]) & (moves[2] == moves[6]) & (moves[2] != ''):
                if moves[2] == 'X':
                    text = 'player wins'
                elif moves[2] == 'O':
                    text = 'ai wins'

            if text != '':
                msg = QMessageBox()
                msg.setWindowTitle('GAME OVER')
                msg.setIcon(QMessageBox.Warning)
                msg.setText(text)

                x = msg.exec_()

                for b in buttons:
                    b.setText('')
                    b.setEnabled(True)

                self.ui.label_2.setText('0'),

                pla = int(self.ui.lbl_player.text())
                a = int(self.ui.lbl_ai.text())
                if text == 'player wins':
                    pla = pla + 1
                elif text == 'ai wins':
                    a = a + 1

                self.ui.lbl_player.setText(str(pla))
                self.ui.lbl_ai.setText(str(a))
        
        self.ui.label.setText(turn)

        #if turn == 'player':
         #   btn.setText('X')
          #  turn = 'ai'
           # self.ui.label.setText('AI TURN')
        #else:
         #   btn.setText('O')
          #  turn = 'player'
           # self.ui.label.setText('PLAYER TURN')

        #buttons = self.ui.gridLayout_2.findChildren(QtWidgets.QPushButton)
        #items = self.ui.centralwidget.findChildren(QtWidgets.QPushButton)
    
    def click_exit(self):
        QtWidgets.qApp.quit()

def app():
    app = QtWidgets.QApplication(sys.argv)
    window = xoxGame()
    window.show()
    sys.exit(app.exec_())

app()