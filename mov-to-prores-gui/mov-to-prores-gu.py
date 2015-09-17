import sys
import os
from PyQt4 import QtGui
from PyQt4.QtCore import *


class MovToProres(QtGui.QMainWindow):
    
    def __init__(self):
        super(MovToProres, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.convert_fname = ''

        self.label_open = QtGui.QLabel()
        self.setCentralWidget(self.label_open)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        convertFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Convert', self)
        convertFile.setStatusTip('Convert to prores')
        convertFile.triggered.connect(self._convert)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        
        fileMenu = menubar.addMenu('&Convert')
        fileMenu.addAction(convertFile)
        
        self.setGeometry(300, 300, 450, 100)
        self.setWindowTitle('Mov to ProRes 4444 (1080p)')
        self.show()
        
    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '*.*')

        self.label_open.setText(fname)
        self.convert_fname  = str(fname[:-4])+'_prores.mov'        

    def _convert(self):

        self.statusBar().showMessage('Start encoding')
        os.system('ffmbc.exe -i '+str(self.label_open.text())+
                  ' -vcodec prores -profile hq -pix_fmt yuv444p10 '+self.convert_fname)
        self.statusBar().showMessage('Final encoding')
        self.label_open.setText(self.convert_fname)
                                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MovToProres()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
